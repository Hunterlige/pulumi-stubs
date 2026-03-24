import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AspectTypeIamBindingConditionArgs",
    "AspectTypeIamBindingConditionArgsDict",
    "AspectTypeIamMemberConditionArgs",
    "AspectTypeIamMemberConditionArgsDict",
    "AssetDiscoverySpecArgs",
    "AssetDiscoverySpecArgsDict",
    "AssetDiscoverySpecCsvOptionsArgs",
    "AssetDiscoverySpecCsvOptionsArgsDict",
    "AssetDiscoverySpecJsonOptionsArgs",
    "AssetDiscoverySpecJsonOptionsArgsDict",
    "AssetDiscoveryStatusArgs",
    "AssetDiscoveryStatusArgsDict",
    "AssetDiscoveryStatusStatArgs",
    "AssetDiscoveryStatusStatArgsDict",
    "AssetIamBindingConditionArgs",
    "AssetIamBindingConditionArgsDict",
    "AssetIamMemberConditionArgs",
    "AssetIamMemberConditionArgsDict",
    "AssetResourceSpecArgs",
    "AssetResourceSpecArgsDict",
    "AssetResourceStatusArgs",
    "AssetResourceStatusArgsDict",
    "AssetSecurityStatusArgs",
    "AssetSecurityStatusArgsDict",
    "DataAssetAccessGroupConfigArgs",
    "DataAssetAccessGroupConfigArgsDict",
    "DataProductAccessGroupArgs",
    "DataProductAccessGroupArgsDict",
    "DataProductAccessGroupPrincipalArgs",
    "DataProductAccessGroupPrincipalArgsDict",
    "DataProductDataAssetAccessGroupConfigArgs",
    "DataProductDataAssetAccessGroupConfigArgsDict",
    "DatascanDataArgs",
    "DatascanDataArgsDict",
    "DatascanDataDiscoverySpecArgs",
    "DatascanDataDiscoverySpecArgsDict",
    ...,
    ...,
    "DatascanDataDiscoverySpecStorageConfigArgs",
    "DatascanDataDiscoverySpecStorageConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "DatascanDataDocumentationSpecArgs",
    "DatascanDataDocumentationSpecArgsDict",
    "DatascanDataProfileSpecArgs",
    "DatascanDataProfileSpecArgsDict",
    "DatascanDataProfileSpecExcludeFieldsArgs",
    "DatascanDataProfileSpecExcludeFieldsArgsDict",
    "DatascanDataProfileSpecIncludeFieldsArgs",
    "DatascanDataProfileSpecIncludeFieldsArgsDict",
    "DatascanDataProfileSpecPostScanActionsArgs",
    "DatascanDataProfileSpecPostScanActionsArgsDict",
    ...,
    ...,
    "DatascanDataQualitySpecArgs",
    "DatascanDataQualitySpecArgsDict",
    "DatascanDataQualitySpecPostScanActionsArgs",
    "DatascanDataQualitySpecPostScanActionsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DatascanDataQualitySpecRuleArgs",
    "DatascanDataQualitySpecRuleArgsDict",
    "DatascanDataQualitySpecRuleNonNullExpectationArgs",
    ...,
    "DatascanDataQualitySpecRuleRangeExpectationArgs",
    ...,
    "DatascanDataQualitySpecRuleRegexExpectationArgs",
    ...,
    ...,
    ...,
    "DatascanDataQualitySpecRuleSetExpectationArgs",
    "DatascanDataQualitySpecRuleSetExpectationArgsDict",
    "DatascanDataQualitySpecRuleSqlAssertionArgs",
    "DatascanDataQualitySpecRuleSqlAssertionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DatascanExecutionSpecArgs",
    "DatascanExecutionSpecArgsDict",
    "DatascanExecutionSpecTriggerArgs",
    "DatascanExecutionSpecTriggerArgsDict",
    "DatascanExecutionSpecTriggerOnDemandArgs",
    "DatascanExecutionSpecTriggerOnDemandArgsDict",
    "DatascanExecutionSpecTriggerOneTimeArgs",
    "DatascanExecutionSpecTriggerOneTimeArgsDict",
    "DatascanExecutionSpecTriggerScheduleArgs",
    "DatascanExecutionSpecTriggerScheduleArgsDict",
    "DatascanExecutionStatusArgs",
    "DatascanExecutionStatusArgsDict",
    "DatascanIamBindingConditionArgs",
    "DatascanIamBindingConditionArgsDict",
    "DatascanIamMemberConditionArgs",
    "DatascanIamMemberConditionArgsDict",
    "EntryAspectArgs",
    "EntryAspectArgsDict",
    "EntryAspectAspectArgs",
    "EntryAspectAspectArgsDict",
    "EntryEntrySourceArgs",
    "EntryEntrySourceArgsDict",
    "EntryEntrySourceAncestorArgs",
    "EntryEntrySourceAncestorArgsDict",
    "EntryGroupIamBindingConditionArgs",
    "EntryGroupIamBindingConditionArgsDict",
    "EntryGroupIamMemberConditionArgs",
    "EntryGroupIamMemberConditionArgsDict",
    "EntryLinkEntryReferenceArgs",
    "EntryLinkEntryReferenceArgsDict",
    "EntryTypeIamBindingConditionArgs",
    "EntryTypeIamBindingConditionArgsDict",
    "EntryTypeIamMemberConditionArgs",
    "EntryTypeIamMemberConditionArgsDict",
    "EntryTypeRequiredAspectArgs",
    "EntryTypeRequiredAspectArgsDict",
    "GlossaryIamBindingConditionArgs",
    "GlossaryIamBindingConditionArgsDict",
    "GlossaryIamMemberConditionArgs",
    "GlossaryIamMemberConditionArgsDict",
    "LakeAssetStatusArgs",
    "LakeAssetStatusArgsDict",
    "LakeIamBindingConditionArgs",
    "LakeIamBindingConditionArgsDict",
    "LakeIamMemberConditionArgs",
    "LakeIamMemberConditionArgsDict",
    "LakeMetastoreArgs",
    "LakeMetastoreArgsDict",
    "LakeMetastoreStatusArgs",
    "LakeMetastoreStatusArgsDict",
    "TaskExecutionSpecArgs",
    "TaskExecutionSpecArgsDict",
    "TaskExecutionStatusArgs",
    "TaskExecutionStatusArgsDict",
    "TaskExecutionStatusLatestJobArgs",
    "TaskExecutionStatusLatestJobArgsDict",
    "TaskIamBindingConditionArgs",
    "TaskIamBindingConditionArgsDict",
    "TaskIamMemberConditionArgs",
    "TaskIamMemberConditionArgsDict",
    "TaskNotebookArgs",
    "TaskNotebookArgsDict",
    "TaskNotebookInfrastructureSpecArgs",
    "TaskNotebookInfrastructureSpecArgsDict",
    "TaskNotebookInfrastructureSpecBatchArgs",
    "TaskNotebookInfrastructureSpecBatchArgsDict",
    "TaskNotebookInfrastructureSpecContainerImageArgs",
    ...,
    "TaskNotebookInfrastructureSpecVpcNetworkArgs",
    "TaskNotebookInfrastructureSpecVpcNetworkArgsDict",
    "TaskSparkArgs",
    "TaskSparkArgsDict",
    "TaskSparkInfrastructureSpecArgs",
    "TaskSparkInfrastructureSpecArgsDict",
    "TaskSparkInfrastructureSpecBatchArgs",
    "TaskSparkInfrastructureSpecBatchArgsDict",
    "TaskSparkInfrastructureSpecContainerImageArgs",
    "TaskSparkInfrastructureSpecContainerImageArgsDict",
    "TaskSparkInfrastructureSpecVpcNetworkArgs",
    "TaskSparkInfrastructureSpecVpcNetworkArgsDict",
    "TaskTriggerSpecArgs",
    "TaskTriggerSpecArgsDict",
    "ZoneAssetStatusArgs",
    "ZoneAssetStatusArgsDict",
    "ZoneDiscoverySpecArgs",
    "ZoneDiscoverySpecArgsDict",
    "ZoneDiscoverySpecCsvOptionsArgs",
    "ZoneDiscoverySpecCsvOptionsArgsDict",
    "ZoneDiscoverySpecJsonOptionsArgs",
    "ZoneDiscoverySpecJsonOptionsArgsDict",
    "ZoneIamBindingConditionArgs",
    "ZoneIamBindingConditionArgsDict",
    "ZoneIamMemberConditionArgs",
    "ZoneIamMemberConditionArgsDict",
    "ZoneResourceSpecArgs",
    "ZoneResourceSpecArgsDict",
]

class AspectTypeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AspectTypeIamBindingConditionArgs:
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

class AspectTypeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AspectTypeIamMemberConditionArgs:
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

class AssetDiscoverySpecArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    csv_options: NotRequired[pulumi.Input[AssetDiscoverySpecCsvOptionsArgsDict]]
    exclude_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    json_options: NotRequired[pulumi.Input[AssetDiscoverySpecJsonOptionsArgsDict]]
    schedule: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetDiscoverySpecArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        csv_options: Optional[pulumi.Input[AssetDiscoverySpecCsvOptionsArgs]] = ...,
        exclude_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        json_options: Optional[pulumi.Input[AssetDiscoverySpecJsonOptionsArgs]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[pulumi.Input[AssetDiscoverySpecCsvOptionsArgs]]: ...
    @csv_options.setter
    def csv_options(
        self, value: Optional[pulumi.Input[AssetDiscoverySpecCsvOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludePatterns")
    def exclude_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_patterns.setter
    def exclude_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includePatterns")
    def include_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_patterns.setter
    def include_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(
        self,
    ) -> Optional[pulumi.Input[AssetDiscoverySpecJsonOptionsArgs]]: ...
    @json_options.setter
    def json_options(
        self, value: Optional[pulumi.Input[AssetDiscoverySpecJsonOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssetDiscoverySpecCsvOptionsArgsDict(TypedDict):
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    disable_type_inference: NotRequired[pulumi.Input[_builtins.bool]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    header_rows: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AssetDiscoverySpecCsvOptionsArgs:
    def __init__(
        __self__,
        *,
        delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_type_inference: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        header_rows: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_type_inference.setter
    def disable_type_inference(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="headerRows")
    def header_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @header_rows.setter
    def header_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AssetDiscoverySpecJsonOptionsArgsDict(TypedDict):
    disable_type_inference: NotRequired[pulumi.Input[_builtins.bool]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetDiscoverySpecJsonOptionsArgs:
    def __init__(
        __self__,
        *,
        disable_type_inference: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_type_inference.setter
    def disable_type_inference(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssetDiscoveryStatusArgsDict(TypedDict):
    last_run_duration: NotRequired[pulumi.Input[_builtins.str]]
    last_run_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    stats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AssetDiscoveryStatusStatArgsDict]]]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetDiscoveryStatusArgs:
    def __init__(
        __self__,
        *,
        last_run_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        last_run_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        stats: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssetDiscoveryStatusStatArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastRunDuration")
    def last_run_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_run_duration.setter
    def last_run_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRunTime")
    def last_run_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_run_time.setter
    def last_run_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def stats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AssetDiscoveryStatusStatArgs]]]
    ]: ...
    @stats.setter
    def stats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssetDiscoveryStatusStatArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssetDiscoveryStatusStatArgsDict(TypedDict):
    data_items: NotRequired[pulumi.Input[_builtins.int]]
    data_size: NotRequired[pulumi.Input[_builtins.int]]
    filesets: NotRequired[pulumi.Input[_builtins.int]]
    tables: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AssetDiscoveryStatusStatArgs:
    def __init__(
        __self__,
        *,
        data_items: Optional[pulumi.Input[_builtins.int]] = ...,
        data_size: Optional[pulumi.Input[_builtins.int]] = ...,
        filesets: Optional[pulumi.Input[_builtins.int]] = ...,
        tables: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataItems")
    def data_items(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_items.setter
    def data_items(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSize")
    def data_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_size.setter
    def data_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def filesets(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @filesets.setter
    def filesets(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tables.setter
    def tables(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AssetIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetIamBindingConditionArgs:
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

class AssetIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetIamMemberConditionArgs:
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

class AssetResourceSpecArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]
    read_access_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetResourceSpecArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        read_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readAccessMode")
    def read_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read_access_mode.setter
    def read_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssetResourceStatusArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetResourceStatusArgs:
    def __init__(
        __self__,
        *,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssetSecurityStatusArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssetSecurityStatusArgs:
    def __init__(
        __self__,
        *,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataAssetAccessGroupConfigArgsDict(TypedDict):
    access_group: pulumi.Input[_builtins.str]
    iam_roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DataAssetAccessGroupConfigArgs:
    def __init__(
        __self__,
        *,
        access_group: pulumi.Input[_builtins.str],
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessGroup")
    def access_group(self) -> pulumi.Input[_builtins.str]: ...
    @access_group.setter
    def access_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @iam_roles.setter
    def iam_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataProductAccessGroupArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]
    group_id: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    principal: pulumi.Input[DataProductAccessGroupPrincipalArgsDict]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataProductAccessGroupArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        group_id: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        principal: pulumi.Input[DataProductAccessGroupPrincipalArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[_builtins.str]: ...
    @group_id.setter
    def group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[DataProductAccessGroupPrincipalArgs]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[DataProductAccessGroupPrincipalArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataProductAccessGroupPrincipalArgsDict(TypedDict):
    google_group: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataProductAccessGroupPrincipalArgs:
    def __init__(
        __self__, *, google_group: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleGroup")
    def google_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @google_group.setter
    def google_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataProductDataAssetAccessGroupConfigArgsDict(TypedDict):
    access_group: pulumi.Input[_builtins.str]
    iam_roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DataProductDataAssetAccessGroupConfigArgs:
    def __init__(
        __self__,
        *,
        access_group: pulumi.Input[_builtins.str],
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessGroup")
    def access_group(self) -> pulumi.Input[_builtins.str]: ...
    @access_group.setter
    def access_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @iam_roles.setter
    def iam_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DatascanDataArgsDict(TypedDict):
    entity: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanDataArgs:
    def __init__(
        __self__,
        *,
        entity: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity.setter
    def entity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatascanDataDiscoverySpecArgsDict(TypedDict):
    bigquery_publishing_config: NotRequired[
        pulumi.Input[DatascanDataDiscoverySpecBigqueryPublishingConfigArgsDict]
    ]
    storage_config: NotRequired[
        pulumi.Input[DatascanDataDiscoverySpecStorageConfigArgsDict]
    ]
    ...

@pulumi.input_type
class DatascanDataDiscoverySpecArgs:
    def __init__(
        __self__,
        *,
        bigquery_publishing_config: Optional[
            pulumi.Input[DatascanDataDiscoverySpecBigqueryPublishingConfigArgs]
        ] = ...,
        storage_config: Optional[
            pulumi.Input[DatascanDataDiscoverySpecStorageConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryPublishingConfig")
    def bigquery_publishing_config(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataDiscoverySpecBigqueryPublishingConfigArgs]
    ]: ...
    @bigquery_publishing_config.setter
    def bigquery_publishing_config(
        self,
        value: Optional[
            pulumi.Input[DatascanDataDiscoverySpecBigqueryPublishingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageConfig")
    def storage_config(
        self,
    ) -> Optional[pulumi.Input[DatascanDataDiscoverySpecStorageConfigArgs]]: ...
    @storage_config.setter
    def storage_config(
        self, value: Optional[pulumi.Input[DatascanDataDiscoverySpecStorageConfigArgs]]
    ): ...

class DatascanDataDiscoverySpecBigqueryPublishingConfigArgsDict(TypedDict):
    connection: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    project: NotRequired[pulumi.Input[_builtins.str]]
    table_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanDataDiscoverySpecBigqueryPublishingConfigArgs:
    def __init__(
        __self__,
        *,
        connection: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        table_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection.setter
    def connection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_type.setter
    def table_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatascanDataDiscoverySpecStorageConfigArgsDict(TypedDict):
    csv_options: NotRequired[
        pulumi.Input[DatascanDataDiscoverySpecStorageConfigCsvOptionsArgsDict]
    ]
    exclude_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    json_options: NotRequired[
        pulumi.Input[DatascanDataDiscoverySpecStorageConfigJsonOptionsArgsDict]
    ]
    ...

@pulumi.input_type
class DatascanDataDiscoverySpecStorageConfigArgs:
    def __init__(
        __self__,
        *,
        csv_options: Optional[
            pulumi.Input[DatascanDataDiscoverySpecStorageConfigCsvOptionsArgs]
        ] = ...,
        exclude_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        json_options: Optional[
            pulumi.Input[DatascanDataDiscoverySpecStorageConfigJsonOptionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataDiscoverySpecStorageConfigCsvOptionsArgs]
    ]: ...
    @csv_options.setter
    def csv_options(
        self,
        value: Optional[
            pulumi.Input[DatascanDataDiscoverySpecStorageConfigCsvOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludePatterns")
    def exclude_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_patterns.setter
    def exclude_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includePatterns")
    def include_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_patterns.setter
    def include_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataDiscoverySpecStorageConfigJsonOptionsArgs]
    ]: ...
    @json_options.setter
    def json_options(
        self,
        value: Optional[
            pulumi.Input[DatascanDataDiscoverySpecStorageConfigJsonOptionsArgs]
        ],
    ): ...

class DatascanDataDiscoverySpecStorageConfigCsvOptionsArgsDict(TypedDict):
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    header_rows: NotRequired[pulumi.Input[_builtins.int]]
    quote: NotRequired[pulumi.Input[_builtins.str]]
    type_inference_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DatascanDataDiscoverySpecStorageConfigCsvOptionsArgs:
    def __init__(
        __self__,
        *,
        delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        header_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        quote: Optional[pulumi.Input[_builtins.str]] = ...,
        type_inference_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="headerRows")
    def header_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @header_rows.setter
    def header_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def quote(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quote.setter
    def quote(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeInferenceDisabled")
    def type_inference_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @type_inference_disabled.setter
    def type_inference_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DatascanDataDiscoverySpecStorageConfigJsonOptionsArgsDict(TypedDict):
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    type_inference_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DatascanDataDiscoverySpecStorageConfigJsonOptionsArgs:
    def __init__(
        __self__,
        *,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        type_inference_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeInferenceDisabled")
    def type_inference_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @type_inference_disabled.setter
    def type_inference_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DatascanDataDocumentationSpecArgsDict(TypedDict): ...

@pulumi.input_type
class DatascanDataDocumentationSpecArgs:
    def __init__(__self__) -> None: ...

class DatascanDataProfileSpecArgsDict(TypedDict):
    catalog_publishing_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    exclude_fields: NotRequired[
        pulumi.Input[DatascanDataProfileSpecExcludeFieldsArgsDict]
    ]
    include_fields: NotRequired[
        pulumi.Input[DatascanDataProfileSpecIncludeFieldsArgsDict]
    ]
    post_scan_actions: NotRequired[
        pulumi.Input[DatascanDataProfileSpecPostScanActionsArgsDict]
    ]
    row_filter: NotRequired[pulumi.Input[_builtins.str]]
    sampling_percent: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class DatascanDataProfileSpecArgs:
    def __init__(
        __self__,
        *,
        catalog_publishing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclude_fields: Optional[
            pulumi.Input[DatascanDataProfileSpecExcludeFieldsArgs]
        ] = ...,
        include_fields: Optional[
            pulumi.Input[DatascanDataProfileSpecIncludeFieldsArgs]
        ] = ...,
        post_scan_actions: Optional[
            pulumi.Input[DatascanDataProfileSpecPostScanActionsArgs]
        ] = ...,
        row_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_percent: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogPublishingEnabled")
    def catalog_publishing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @catalog_publishing_enabled.setter
    def catalog_publishing_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeFields")
    def exclude_fields(
        self,
    ) -> Optional[pulumi.Input[DatascanDataProfileSpecExcludeFieldsArgs]]: ...
    @exclude_fields.setter
    def exclude_fields(
        self, value: Optional[pulumi.Input[DatascanDataProfileSpecExcludeFieldsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeFields")
    def include_fields(
        self,
    ) -> Optional[pulumi.Input[DatascanDataProfileSpecIncludeFieldsArgs]]: ...
    @include_fields.setter
    def include_fields(
        self, value: Optional[pulumi.Input[DatascanDataProfileSpecIncludeFieldsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="postScanActions")
    def post_scan_actions(
        self,
    ) -> Optional[pulumi.Input[DatascanDataProfileSpecPostScanActionsArgs]]: ...
    @post_scan_actions.setter
    def post_scan_actions(
        self, value: Optional[pulumi.Input[DatascanDataProfileSpecPostScanActionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rowFilter")
    def row_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @row_filter.setter
    def row_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingPercent")
    def sampling_percent(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sampling_percent.setter
    def sampling_percent(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class DatascanDataProfileSpecExcludeFieldsArgsDict(TypedDict):
    field_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DatascanDataProfileSpecExcludeFieldsArgs:
    def __init__(
        __self__,
        *,
        field_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldNames")
    def field_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @field_names.setter
    def field_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DatascanDataProfileSpecIncludeFieldsArgsDict(TypedDict):
    field_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DatascanDataProfileSpecIncludeFieldsArgs:
    def __init__(
        __self__,
        *,
        field_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldNames")
    def field_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @field_names.setter
    def field_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DatascanDataProfileSpecPostScanActionsArgsDict(TypedDict):
    bigquery_export: NotRequired[
        pulumi.Input[DatascanDataProfileSpecPostScanActionsBigqueryExportArgsDict]
    ]
    ...

@pulumi.input_type
class DatascanDataProfileSpecPostScanActionsArgs:
    def __init__(
        __self__,
        *,
        bigquery_export: Optional[
            pulumi.Input[DatascanDataProfileSpecPostScanActionsBigqueryExportArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryExport")
    def bigquery_export(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataProfileSpecPostScanActionsBigqueryExportArgs]
    ]: ...
    @bigquery_export.setter
    def bigquery_export(
        self,
        value: Optional[
            pulumi.Input[DatascanDataProfileSpecPostScanActionsBigqueryExportArgs]
        ],
    ): ...

class DatascanDataProfileSpecPostScanActionsBigqueryExportArgsDict(TypedDict):
    results_table: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanDataProfileSpecPostScanActionsBigqueryExportArgs:
    def __init__(
        __self__, *, results_table: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resultsTable")
    def results_table(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @results_table.setter
    def results_table(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatascanDataQualitySpecArgsDict(TypedDict):
    catalog_publishing_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    post_scan_actions: NotRequired[
        pulumi.Input[DatascanDataQualitySpecPostScanActionsArgsDict]
    ]
    row_filter: NotRequired[pulumi.Input[_builtins.str]]
    rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DatascanDataQualitySpecRuleArgsDict]]]
    ]
    sampling_percent: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class DatascanDataQualitySpecArgs:
    def __init__(
        __self__,
        *,
        catalog_publishing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        post_scan_actions: Optional[
            pulumi.Input[DatascanDataQualitySpecPostScanActionsArgs]
        ] = ...,
        row_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[DatascanDataQualitySpecRuleArgs]]]
        ] = ...,
        sampling_percent: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogPublishingEnabled")
    def catalog_publishing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @catalog_publishing_enabled.setter
    def catalog_publishing_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="postScanActions")
    def post_scan_actions(
        self,
    ) -> Optional[pulumi.Input[DatascanDataQualitySpecPostScanActionsArgs]]: ...
    @post_scan_actions.setter
    def post_scan_actions(
        self, value: Optional[pulumi.Input[DatascanDataQualitySpecPostScanActionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rowFilter")
    def row_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @row_filter.setter
    def row_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DatascanDataQualitySpecRuleArgs]]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DatascanDataQualitySpecRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="samplingPercent")
    def sampling_percent(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sampling_percent.setter
    def sampling_percent(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class DatascanDataQualitySpecPostScanActionsArgsDict(TypedDict):
    bigquery_export: NotRequired[
        pulumi.Input[DatascanDataQualitySpecPostScanActionsBigqueryExportArgsDict]
    ]
    notification_report: NotRequired[
        pulumi.Input[DatascanDataQualitySpecPostScanActionsNotificationReportArgsDict]
    ]
    ...

@pulumi.input_type
class DatascanDataQualitySpecPostScanActionsArgs:
    def __init__(
        __self__,
        *,
        bigquery_export: Optional[
            pulumi.Input[DatascanDataQualitySpecPostScanActionsBigqueryExportArgs]
        ] = ...,
        notification_report: Optional[
            pulumi.Input[DatascanDataQualitySpecPostScanActionsNotificationReportArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryExport")
    def bigquery_export(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataQualitySpecPostScanActionsBigqueryExportArgs]
    ]: ...
    @bigquery_export.setter
    def bigquery_export(
        self,
        value: Optional[
            pulumi.Input[DatascanDataQualitySpecPostScanActionsBigqueryExportArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationReport")
    def notification_report(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataQualitySpecPostScanActionsNotificationReportArgs]
    ]: ...
    @notification_report.setter
    def notification_report(
        self,
        value: Optional[
            pulumi.Input[DatascanDataQualitySpecPostScanActionsNotificationReportArgs]
        ],
    ): ...

class DatascanDataQualitySpecPostScanActionsBigqueryExportArgsDict(TypedDict):
    results_table: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanDataQualitySpecPostScanActionsBigqueryExportArgs:
    def __init__(
        __self__, *, results_table: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resultsTable")
    def results_table(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @results_table.setter
    def results_table(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatascanDataQualitySpecPostScanActionsNotificationReportArgsDict(TypedDict):
    recipients: pulumi.Input[
        DatascanDataQualitySpecPostScanActionsNotificationReportRecipientsArgsDict
    ]
    job_end_trigger: NotRequired[
        pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTriggerArgsDict
        ]
    ]
    job_failure_trigger: NotRequired[
        pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTriggerArgsDict
        ]
    ]
    score_threshold_trigger: NotRequired[
        pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTriggerArgsDict
        ]
    ]
    ...

@pulumi.input_type
class DatascanDataQualitySpecPostScanActionsNotificationReportArgs:
    def __init__(
        __self__,
        *,
        recipients: pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportRecipientsArgs
        ],
        job_end_trigger: Optional[
            pulumi.Input[
                DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTriggerArgs
            ]
        ] = ...,
        job_failure_trigger: Optional[
            pulumi.Input[
                DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTriggerArgs
            ]
        ] = ...,
        score_threshold_trigger: Optional[
            pulumi.Input[
                DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTriggerArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recipients(
        self,
    ) -> pulumi.Input[
        DatascanDataQualitySpecPostScanActionsNotificationReportRecipientsArgs
    ]: ...
    @recipients.setter
    def recipients(
        self,
        value: pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportRecipientsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobEndTrigger")
    def job_end_trigger(
        self,
    ) -> Optional[
        pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTriggerArgs
        ]
    ]: ...
    @job_end_trigger.setter
    def job_end_trigger(
        self,
        value: Optional[
            pulumi.Input[
                DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTriggerArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobFailureTrigger")
    def job_failure_trigger(
        self,
    ) -> Optional[
        pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTriggerArgs
        ]
    ]: ...
    @job_failure_trigger.setter
    def job_failure_trigger(
        self,
        value: Optional[
            pulumi.Input[
                DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTriggerArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scoreThresholdTrigger")
    def score_threshold_trigger(
        self,
    ) -> Optional[
        pulumi.Input[
            DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTriggerArgs
        ]
    ]: ...
    @score_threshold_trigger.setter
    def score_threshold_trigger(
        self,
        value: Optional[
            pulumi.Input[
                DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTriggerArgs
            ]
        ],
    ): ...

class DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTriggerArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTriggerArgs:
    def __init__(__self__) -> None: ...

class DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTriggerArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTriggerArgs:
    def __init__(__self__) -> None: ...

class DatascanDataQualitySpecPostScanActionsNotificationReportRecipientsArgsDict(
    TypedDict
):
    emails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DatascanDataQualitySpecPostScanActionsNotificationReportRecipientsArgs:
    def __init__(
        __self__,
        *,
        emails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @emails.setter
    def emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTriggerArgsDict(
    TypedDict
):
    score_threshold: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTriggerArgs:
    def __init__(
        __self__, *, score_threshold: Optional[pulumi.Input[_builtins.float]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scoreThreshold")
    def score_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @score_threshold.setter
    def score_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class DatascanDataQualitySpecRuleArgsDict(TypedDict):
    dimension: pulumi.Input[_builtins.str]
    column: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ignore_null: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    non_null_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleNonNullExpectationArgsDict]
    ]
    range_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleRangeExpectationArgsDict]
    ]
    regex_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleRegexExpectationArgsDict]
    ]
    row_condition_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleRowConditionExpectationArgsDict]
    ]
    set_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleSetExpectationArgsDict]
    ]
    sql_assertion: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleSqlAssertionArgsDict]
    ]
    statistic_range_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleStatisticRangeExpectationArgsDict]
    ]
    suspended: NotRequired[pulumi.Input[_builtins.bool]]
    table_condition_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleTableConditionExpectationArgsDict]
    ]
    threshold: NotRequired[pulumi.Input[_builtins.float]]
    uniqueness_expectation: NotRequired[
        pulumi.Input[DatascanDataQualitySpecRuleUniquenessExpectationArgsDict]
    ]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleArgs:
    def __init__(
        __self__,
        *,
        dimension: pulumi.Input[_builtins.str],
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_null: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        non_null_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleNonNullExpectationArgs]
        ] = ...,
        range_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleRangeExpectationArgs]
        ] = ...,
        regex_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleRegexExpectationArgs]
        ] = ...,
        row_condition_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleRowConditionExpectationArgs]
        ] = ...,
        set_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleSetExpectationArgs]
        ] = ...,
        sql_assertion: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleSqlAssertionArgs]
        ] = ...,
        statistic_range_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleStatisticRangeExpectationArgs]
        ] = ...,
        suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
        table_condition_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleTableConditionExpectationArgs]
        ] = ...,
        threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        uniqueness_expectation: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleUniquenessExpectationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> pulumi.Input[_builtins.str]: ...
    @dimension.setter
    def dimension(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreNull")
    def ignore_null(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_null.setter
    def ignore_null(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nonNullExpectation")
    def non_null_expectation(
        self,
    ) -> Optional[pulumi.Input[DatascanDataQualitySpecRuleNonNullExpectationArgs]]: ...
    @non_null_expectation.setter
    def non_null_expectation(
        self,
        value: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleNonNullExpectationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rangeExpectation")
    def range_expectation(
        self,
    ) -> Optional[pulumi.Input[DatascanDataQualitySpecRuleRangeExpectationArgs]]: ...
    @range_expectation.setter
    def range_expectation(
        self,
        value: Optional[pulumi.Input[DatascanDataQualitySpecRuleRangeExpectationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regexExpectation")
    def regex_expectation(
        self,
    ) -> Optional[pulumi.Input[DatascanDataQualitySpecRuleRegexExpectationArgs]]: ...
    @regex_expectation.setter
    def regex_expectation(
        self,
        value: Optional[pulumi.Input[DatascanDataQualitySpecRuleRegexExpectationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rowConditionExpectation")
    def row_condition_expectation(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataQualitySpecRuleRowConditionExpectationArgs]
    ]: ...
    @row_condition_expectation.setter
    def row_condition_expectation(
        self,
        value: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleRowConditionExpectationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="setExpectation")
    def set_expectation(
        self,
    ) -> Optional[pulumi.Input[DatascanDataQualitySpecRuleSetExpectationArgs]]: ...
    @set_expectation.setter
    def set_expectation(
        self,
        value: Optional[pulumi.Input[DatascanDataQualitySpecRuleSetExpectationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlAssertion")
    def sql_assertion(
        self,
    ) -> Optional[pulumi.Input[DatascanDataQualitySpecRuleSqlAssertionArgs]]: ...
    @sql_assertion.setter
    def sql_assertion(
        self, value: Optional[pulumi.Input[DatascanDataQualitySpecRuleSqlAssertionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="statisticRangeExpectation")
    def statistic_range_expectation(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataQualitySpecRuleStatisticRangeExpectationArgs]
    ]: ...
    @statistic_range_expectation.setter
    def statistic_range_expectation(
        self,
        value: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleStatisticRangeExpectationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def suspended(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @suspended.setter
    def suspended(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="tableConditionExpectation")
    def table_condition_expectation(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataQualitySpecRuleTableConditionExpectationArgs]
    ]: ...
    @table_condition_expectation.setter
    def table_condition_expectation(
        self,
        value: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleTableConditionExpectationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="uniquenessExpectation")
    def uniqueness_expectation(
        self,
    ) -> Optional[
        pulumi.Input[DatascanDataQualitySpecRuleUniquenessExpectationArgs]
    ]: ...
    @uniqueness_expectation.setter
    def uniqueness_expectation(
        self,
        value: Optional[
            pulumi.Input[DatascanDataQualitySpecRuleUniquenessExpectationArgs]
        ],
    ): ...

class DatascanDataQualitySpecRuleNonNullExpectationArgsDict(TypedDict): ...

@pulumi.input_type
class DatascanDataQualitySpecRuleNonNullExpectationArgs:
    def __init__(__self__) -> None: ...

class DatascanDataQualitySpecRuleRangeExpectationArgsDict(TypedDict):
    max_value: NotRequired[pulumi.Input[_builtins.str]]
    min_value: NotRequired[pulumi.Input[_builtins.str]]
    strict_max_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    strict_min_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleRangeExpectationArgs:
    def __init__(
        __self__,
        *,
        max_value: Optional[pulumi.Input[_builtins.str]] = ...,
        min_value: Optional[pulumi.Input[_builtins.str]] = ...,
        strict_max_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        strict_min_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strictMaxEnabled")
    def strict_max_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @strict_max_enabled.setter
    def strict_max_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="strictMinEnabled")
    def strict_min_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @strict_min_enabled.setter
    def strict_min_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DatascanDataQualitySpecRuleRegexExpectationArgsDict(TypedDict):
    regex: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleRegexExpectationArgs:
    def __init__(__self__, *, regex: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> pulumi.Input[_builtins.str]: ...
    @regex.setter
    def regex(self, value: pulumi.Input[_builtins.str]): ...

class DatascanDataQualitySpecRuleRowConditionExpectationArgsDict(TypedDict):
    sql_expression: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleRowConditionExpectationArgs:
    def __init__(__self__, *, sql_expression: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> pulumi.Input[_builtins.str]: ...
    @sql_expression.setter
    def sql_expression(self, value: pulumi.Input[_builtins.str]): ...

class DatascanDataQualitySpecRuleSetExpectationArgsDict(TypedDict):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleSetExpectationArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class DatascanDataQualitySpecRuleSqlAssertionArgsDict(TypedDict):
    sql_statement: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleSqlAssertionArgs:
    def __init__(__self__, *, sql_statement: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlStatement")
    def sql_statement(self) -> pulumi.Input[_builtins.str]: ...
    @sql_statement.setter
    def sql_statement(self, value: pulumi.Input[_builtins.str]): ...

class DatascanDataQualitySpecRuleStatisticRangeExpectationArgsDict(TypedDict):
    statistic: pulumi.Input[_builtins.str]
    max_value: NotRequired[pulumi.Input[_builtins.str]]
    min_value: NotRequired[pulumi.Input[_builtins.str]]
    strict_max_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    strict_min_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleStatisticRangeExpectationArgs:
    def __init__(
        __self__,
        *,
        statistic: pulumi.Input[_builtins.str],
        max_value: Optional[pulumi.Input[_builtins.str]] = ...,
        min_value: Optional[pulumi.Input[_builtins.str]] = ...,
        strict_max_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        strict_min_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> pulumi.Input[_builtins.str]: ...
    @statistic.setter
    def statistic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strictMaxEnabled")
    def strict_max_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @strict_max_enabled.setter
    def strict_max_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="strictMinEnabled")
    def strict_min_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @strict_min_enabled.setter
    def strict_min_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DatascanDataQualitySpecRuleTableConditionExpectationArgsDict(TypedDict):
    sql_expression: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DatascanDataQualitySpecRuleTableConditionExpectationArgs:
    def __init__(__self__, *, sql_expression: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> pulumi.Input[_builtins.str]: ...
    @sql_expression.setter
    def sql_expression(self, value: pulumi.Input[_builtins.str]): ...

class DatascanDataQualitySpecRuleUniquenessExpectationArgsDict(TypedDict): ...

@pulumi.input_type
class DatascanDataQualitySpecRuleUniquenessExpectationArgs:
    def __init__(__self__) -> None: ...

class DatascanExecutionSpecArgsDict(TypedDict):
    trigger: pulumi.Input[DatascanExecutionSpecTriggerArgsDict]
    field: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanExecutionSpecArgs:
    def __init__(
        __self__,
        *,
        trigger: pulumi.Input[DatascanExecutionSpecTriggerArgs],
        field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> pulumi.Input[DatascanExecutionSpecTriggerArgs]: ...
    @trigger.setter
    def trigger(self, value: pulumi.Input[DatascanExecutionSpecTriggerArgs]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatascanExecutionSpecTriggerArgsDict(TypedDict):
    on_demand: NotRequired[pulumi.Input[DatascanExecutionSpecTriggerOnDemandArgsDict]]
    one_time: NotRequired[pulumi.Input[DatascanExecutionSpecTriggerOneTimeArgsDict]]
    schedule: NotRequired[pulumi.Input[DatascanExecutionSpecTriggerScheduleArgsDict]]
    ...

@pulumi.input_type
class DatascanExecutionSpecTriggerArgs:
    def __init__(
        __self__,
        *,
        on_demand: Optional[
            pulumi.Input[DatascanExecutionSpecTriggerOnDemandArgs]
        ] = ...,
        one_time: Optional[pulumi.Input[DatascanExecutionSpecTriggerOneTimeArgs]] = ...,
        schedule: Optional[
            pulumi.Input[DatascanExecutionSpecTriggerScheduleArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemand")
    def on_demand(
        self,
    ) -> Optional[pulumi.Input[DatascanExecutionSpecTriggerOnDemandArgs]]: ...
    @on_demand.setter
    def on_demand(
        self, value: Optional[pulumi.Input[DatascanExecutionSpecTriggerOnDemandArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oneTime")
    def one_time(
        self,
    ) -> Optional[pulumi.Input[DatascanExecutionSpecTriggerOneTimeArgs]]: ...
    @one_time.setter
    def one_time(
        self, value: Optional[pulumi.Input[DatascanExecutionSpecTriggerOneTimeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(
        self,
    ) -> Optional[pulumi.Input[DatascanExecutionSpecTriggerScheduleArgs]]: ...
    @schedule.setter
    def schedule(
        self, value: Optional[pulumi.Input[DatascanExecutionSpecTriggerScheduleArgs]]
    ): ...

class DatascanExecutionSpecTriggerOnDemandArgsDict(TypedDict): ...

@pulumi.input_type
class DatascanExecutionSpecTriggerOnDemandArgs:
    def __init__(__self__) -> None: ...

class DatascanExecutionSpecTriggerOneTimeArgsDict(TypedDict):
    ttl_after_scan_completion: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanExecutionSpecTriggerOneTimeArgs:
    def __init__(
        __self__,
        *,
        ttl_after_scan_completion: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ttlAfterScanCompletion")
    def ttl_after_scan_completion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ttl_after_scan_completion.setter
    def ttl_after_scan_completion(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class DatascanExecutionSpecTriggerScheduleArgsDict(TypedDict):
    cron: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DatascanExecutionSpecTriggerScheduleArgs:
    def __init__(__self__, *, cron: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> pulumi.Input[_builtins.str]: ...
    @cron.setter
    def cron(self, value: pulumi.Input[_builtins.str]): ...

class DatascanExecutionStatusArgsDict(TypedDict):
    latest_job_end_time: NotRequired[pulumi.Input[_builtins.str]]
    latest_job_start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanExecutionStatusArgs:
    def __init__(
        __self__,
        *,
        latest_job_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_job_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestJobEndTime")
    def latest_job_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_job_end_time.setter
    def latest_job_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latestJobStartTime")
    def latest_job_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_job_start_time.setter
    def latest_job_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatascanIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanIamBindingConditionArgs:
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

class DatascanIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatascanIamMemberConditionArgs:
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

class EntryAspectArgsDict(TypedDict):
    aspect: pulumi.Input[EntryAspectAspectArgsDict]
    aspect_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EntryAspectArgs:
    def __init__(
        __self__,
        *,
        aspect: pulumi.Input[EntryAspectAspectArgs],
        aspect_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aspect(self) -> pulumi.Input[EntryAspectAspectArgs]: ...
    @aspect.setter
    def aspect(self, value: pulumi.Input[EntryAspectAspectArgs]): ...
    @_builtins.property
    @pulumi.getter(name="aspectKey")
    def aspect_key(self) -> pulumi.Input[_builtins.str]: ...
    @aspect_key.setter
    def aspect_key(self, value: pulumi.Input[_builtins.str]): ...

class EntryAspectAspectArgsDict(TypedDict):
    data: pulumi.Input[_builtins.str]
    aspect_type: NotRequired[pulumi.Input[_builtins.str]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryAspectAspectArgs:
    def __init__(
        __self__,
        *,
        data: pulumi.Input[_builtins.str],
        aspect_type: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> pulumi.Input[_builtins.str]: ...
    @data.setter
    def data(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="aspectType")
    def aspect_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aspect_type.setter
    def aspect_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntryEntrySourceArgsDict(TypedDict):
    ancestors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EntryEntrySourceAncestorArgsDict]]]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    platform: NotRequired[pulumi.Input[_builtins.str]]
    resource: NotRequired[pulumi.Input[_builtins.str]]
    system: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryEntrySourceArgs:
    def __init__(
        __self__,
        *,
        ancestors: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryEntrySourceAncestorArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
        system: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ancestors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EntryEntrySourceAncestorArgs]]]
    ]: ...
    @ancestors.setter
    def ancestors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryEntrySourceAncestorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @system.setter
    def system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntryEntrySourceAncestorArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryEntrySourceAncestorArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntryGroupIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryGroupIamBindingConditionArgs:
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

class EntryGroupIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryGroupIamMemberConditionArgs:
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

class EntryLinkEntryReferenceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryLinkEntryReferenceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntryTypeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryTypeIamBindingConditionArgs:
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

class EntryTypeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryTypeIamMemberConditionArgs:
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

class EntryTypeRequiredAspectArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EntryTypeRequiredAspectArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GlossaryIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GlossaryIamBindingConditionArgs:
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

class GlossaryIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GlossaryIamMemberConditionArgs:
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

class LakeAssetStatusArgsDict(TypedDict):
    active_assets: NotRequired[pulumi.Input[_builtins.int]]
    security_policy_applying_assets: NotRequired[pulumi.Input[_builtins.int]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LakeAssetStatusArgs:
    def __init__(
        __self__,
        *,
        active_assets: Optional[pulumi.Input[_builtins.int]] = ...,
        security_policy_applying_assets: Optional[pulumi.Input[_builtins.int]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeAssets")
    def active_assets(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @active_assets.setter
    def active_assets(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyApplyingAssets")
    def security_policy_applying_assets(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @security_policy_applying_assets.setter
    def security_policy_applying_assets(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LakeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LakeIamBindingConditionArgs:
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

class LakeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LakeIamMemberConditionArgs:
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

class LakeMetastoreArgsDict(TypedDict):
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LakeMetastoreArgs:
    def __init__(
        __self__, *, service: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LakeMetastoreStatusArgsDict(TypedDict):
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LakeMetastoreStatusArgs:
    def __init__(
        __self__,
        *,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskExecutionSpecArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    max_job_execution_lifetime: NotRequired[pulumi.Input[_builtins.str]]
    project: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskExecutionSpecArgs:
    def __init__(
        __self__,
        *,
        service_account: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        max_job_execution_lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxJobExecutionLifetime")
    def max_job_execution_lifetime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_job_execution_lifetime.setter
    def max_job_execution_lifetime(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskExecutionStatusArgsDict(TypedDict):
    latest_jobs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TaskExecutionStatusLatestJobArgsDict]]]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskExecutionStatusArgs:
    def __init__(
        __self__,
        *,
        latest_jobs: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskExecutionStatusLatestJobArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestJobs")
    def latest_jobs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TaskExecutionStatusLatestJobArgs]]]
    ]: ...
    @latest_jobs.setter
    def latest_jobs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskExecutionStatusLatestJobArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskExecutionStatusLatestJobArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    retry_count: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    service_job: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskExecutionStatusLatestJobArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_count: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        service_job: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_count.setter
    def retry_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceJob")
    def service_job(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_job.setter
    def service_job(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskIamBindingConditionArgs:
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

class TaskIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskIamMemberConditionArgs:
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

class TaskNotebookArgsDict(TypedDict):
    notebook: pulumi.Input[_builtins.str]
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    infrastructure_spec: NotRequired[
        pulumi.Input[TaskNotebookInfrastructureSpecArgsDict]
    ]
    ...

@pulumi.input_type
class TaskNotebookArgs:
    def __init__(
        __self__,
        *,
        notebook: pulumi.Input[_builtins.str],
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        infrastructure_spec: Optional[
            pulumi.Input[TaskNotebookInfrastructureSpecArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def notebook(self) -> pulumi.Input[_builtins.str]: ...
    @notebook.setter
    def notebook(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureSpec")
    def infrastructure_spec(
        self,
    ) -> Optional[pulumi.Input[TaskNotebookInfrastructureSpecArgs]]: ...
    @infrastructure_spec.setter
    def infrastructure_spec(
        self, value: Optional[pulumi.Input[TaskNotebookInfrastructureSpecArgs]]
    ): ...

class TaskNotebookInfrastructureSpecArgsDict(TypedDict):
    batch: NotRequired[pulumi.Input[TaskNotebookInfrastructureSpecBatchArgsDict]]
    container_image: NotRequired[
        pulumi.Input[TaskNotebookInfrastructureSpecContainerImageArgsDict]
    ]
    vpc_network: NotRequired[
        pulumi.Input[TaskNotebookInfrastructureSpecVpcNetworkArgsDict]
    ]
    ...

@pulumi.input_type
class TaskNotebookInfrastructureSpecArgs:
    def __init__(
        __self__,
        *,
        batch: Optional[pulumi.Input[TaskNotebookInfrastructureSpecBatchArgs]] = ...,
        container_image: Optional[
            pulumi.Input[TaskNotebookInfrastructureSpecContainerImageArgs]
        ] = ...,
        vpc_network: Optional[
            pulumi.Input[TaskNotebookInfrastructureSpecVpcNetworkArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def batch(
        self,
    ) -> Optional[pulumi.Input[TaskNotebookInfrastructureSpecBatchArgs]]: ...
    @batch.setter
    def batch(
        self, value: Optional[pulumi.Input[TaskNotebookInfrastructureSpecBatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(
        self,
    ) -> Optional[pulumi.Input[TaskNotebookInfrastructureSpecContainerImageArgs]]: ...
    @container_image.setter
    def container_image(
        self,
        value: Optional[pulumi.Input[TaskNotebookInfrastructureSpecContainerImageArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcNetwork")
    def vpc_network(
        self,
    ) -> Optional[pulumi.Input[TaskNotebookInfrastructureSpecVpcNetworkArgs]]: ...
    @vpc_network.setter
    def vpc_network(
        self,
        value: Optional[pulumi.Input[TaskNotebookInfrastructureSpecVpcNetworkArgs]],
    ): ...

class TaskNotebookInfrastructureSpecBatchArgsDict(TypedDict):
    executors_count: NotRequired[pulumi.Input[_builtins.int]]
    max_executors_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class TaskNotebookInfrastructureSpecBatchArgs:
    def __init__(
        __self__,
        *,
        executors_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_executors_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executorsCount")
    def executors_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @executors_count.setter
    def executors_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxExecutorsCount")
    def max_executors_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_executors_count.setter
    def max_executors_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TaskNotebookInfrastructureSpecContainerImageArgsDict(TypedDict):
    image: NotRequired[pulumi.Input[_builtins.str]]
    java_jars: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    python_packages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class TaskNotebookInfrastructureSpecContainerImageArgs:
    def __init__(
        __self__,
        *,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        java_jars: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        python_packages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="javaJars")
    def java_jars(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @java_jars.setter
    def java_jars(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @python_packages.setter
    def python_packages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TaskNotebookInfrastructureSpecVpcNetworkArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    network_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sub_network: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskNotebookInfrastructureSpecVpcNetworkArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        sub_network: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_tags.setter
    def network_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subNetwork")
    def sub_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_network.setter
    def sub_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskSparkArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    infrastructure_spec: NotRequired[pulumi.Input[TaskSparkInfrastructureSpecArgsDict]]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_jar_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    python_script_file: NotRequired[pulumi.Input[_builtins.str]]
    sql_script: NotRequired[pulumi.Input[_builtins.str]]
    sql_script_file: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskSparkArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        infrastructure_spec: Optional[
            pulumi.Input[TaskSparkInfrastructureSpecArgs]
        ] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_jar_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        python_script_file: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_script: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_script_file: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureSpec")
    def infrastructure_spec(
        self,
    ) -> Optional[pulumi.Input[TaskSparkInfrastructureSpecArgs]]: ...
    @infrastructure_spec.setter
    def infrastructure_spec(
        self, value: Optional[pulumi.Input[TaskSparkInfrastructureSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonScriptFile")
    def python_script_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_script_file.setter
    def python_script_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlScript")
    def sql_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql_script.setter
    def sql_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlScriptFile")
    def sql_script_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql_script_file.setter
    def sql_script_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskSparkInfrastructureSpecArgsDict(TypedDict):
    batch: NotRequired[pulumi.Input[TaskSparkInfrastructureSpecBatchArgsDict]]
    container_image: NotRequired[
        pulumi.Input[TaskSparkInfrastructureSpecContainerImageArgsDict]
    ]
    vpc_network: NotRequired[
        pulumi.Input[TaskSparkInfrastructureSpecVpcNetworkArgsDict]
    ]
    ...

@pulumi.input_type
class TaskSparkInfrastructureSpecArgs:
    def __init__(
        __self__,
        *,
        batch: Optional[pulumi.Input[TaskSparkInfrastructureSpecBatchArgs]] = ...,
        container_image: Optional[
            pulumi.Input[TaskSparkInfrastructureSpecContainerImageArgs]
        ] = ...,
        vpc_network: Optional[
            pulumi.Input[TaskSparkInfrastructureSpecVpcNetworkArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def batch(self) -> Optional[pulumi.Input[TaskSparkInfrastructureSpecBatchArgs]]: ...
    @batch.setter
    def batch(
        self, value: Optional[pulumi.Input[TaskSparkInfrastructureSpecBatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(
        self,
    ) -> Optional[pulumi.Input[TaskSparkInfrastructureSpecContainerImageArgs]]: ...
    @container_image.setter
    def container_image(
        self,
        value: Optional[pulumi.Input[TaskSparkInfrastructureSpecContainerImageArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcNetwork")
    def vpc_network(
        self,
    ) -> Optional[pulumi.Input[TaskSparkInfrastructureSpecVpcNetworkArgs]]: ...
    @vpc_network.setter
    def vpc_network(
        self, value: Optional[pulumi.Input[TaskSparkInfrastructureSpecVpcNetworkArgs]]
    ): ...

class TaskSparkInfrastructureSpecBatchArgsDict(TypedDict):
    executors_count: NotRequired[pulumi.Input[_builtins.int]]
    max_executors_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class TaskSparkInfrastructureSpecBatchArgs:
    def __init__(
        __self__,
        *,
        executors_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_executors_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executorsCount")
    def executors_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @executors_count.setter
    def executors_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxExecutorsCount")
    def max_executors_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_executors_count.setter
    def max_executors_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TaskSparkInfrastructureSpecContainerImageArgsDict(TypedDict):
    image: NotRequired[pulumi.Input[_builtins.str]]
    java_jars: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    python_packages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class TaskSparkInfrastructureSpecContainerImageArgs:
    def __init__(
        __self__,
        *,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        java_jars: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        python_packages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="javaJars")
    def java_jars(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @java_jars.setter
    def java_jars(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @python_packages.setter
    def python_packages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TaskSparkInfrastructureSpecVpcNetworkArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    network_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sub_network: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskSparkInfrastructureSpecVpcNetworkArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        sub_network: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_tags.setter
    def network_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subNetwork")
    def sub_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_network.setter
    def sub_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskTriggerSpecArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_retries: NotRequired[pulumi.Input[_builtins.int]]
    schedule: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TaskTriggerSpecArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ZoneAssetStatusArgsDict(TypedDict):
    active_assets: NotRequired[pulumi.Input[_builtins.int]]
    security_policy_applying_assets: NotRequired[pulumi.Input[_builtins.int]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ZoneAssetStatusArgs:
    def __init__(
        __self__,
        *,
        active_assets: Optional[pulumi.Input[_builtins.int]] = ...,
        security_policy_applying_assets: Optional[pulumi.Input[_builtins.int]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeAssets")
    def active_assets(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @active_assets.setter
    def active_assets(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyApplyingAssets")
    def security_policy_applying_assets(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @security_policy_applying_assets.setter
    def security_policy_applying_assets(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ZoneDiscoverySpecArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    csv_options: NotRequired[pulumi.Input[ZoneDiscoverySpecCsvOptionsArgsDict]]
    exclude_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_patterns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    json_options: NotRequired[pulumi.Input[ZoneDiscoverySpecJsonOptionsArgsDict]]
    schedule: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ZoneDiscoverySpecArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        csv_options: Optional[pulumi.Input[ZoneDiscoverySpecCsvOptionsArgs]] = ...,
        exclude_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        json_options: Optional[pulumi.Input[ZoneDiscoverySpecJsonOptionsArgs]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[pulumi.Input[ZoneDiscoverySpecCsvOptionsArgs]]: ...
    @csv_options.setter
    def csv_options(
        self, value: Optional[pulumi.Input[ZoneDiscoverySpecCsvOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludePatterns")
    def exclude_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_patterns.setter
    def exclude_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includePatterns")
    def include_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_patterns.setter
    def include_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(
        self,
    ) -> Optional[pulumi.Input[ZoneDiscoverySpecJsonOptionsArgs]]: ...
    @json_options.setter
    def json_options(
        self, value: Optional[pulumi.Input[ZoneDiscoverySpecJsonOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ZoneDiscoverySpecCsvOptionsArgsDict(TypedDict):
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    disable_type_inference: NotRequired[pulumi.Input[_builtins.bool]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    header_rows: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ZoneDiscoverySpecCsvOptionsArgs:
    def __init__(
        __self__,
        *,
        delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_type_inference: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        header_rows: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_type_inference.setter
    def disable_type_inference(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="headerRows")
    def header_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @header_rows.setter
    def header_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ZoneDiscoverySpecJsonOptionsArgsDict(TypedDict):
    disable_type_inference: NotRequired[pulumi.Input[_builtins.bool]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ZoneDiscoverySpecJsonOptionsArgs:
    def __init__(
        __self__,
        *,
        disable_type_inference: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_type_inference.setter
    def disable_type_inference(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ZoneIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ZoneIamBindingConditionArgs:
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

class ZoneIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ZoneIamMemberConditionArgs:
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

class ZoneResourceSpecArgsDict(TypedDict):
    location_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ZoneResourceSpecArgs:
    def __init__(__self__, *, location_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationType")
    def location_type(self) -> pulumi.Input[_builtins.str]: ...
    @location_type.setter
    def location_type(self, value: pulumi.Input[_builtins.str]): ...

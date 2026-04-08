import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BudgetComparisonExpressionArgs",
    "BudgetComparisonExpressionArgsDict",
    "BudgetFilterPropertiesArgs",
    "BudgetFilterPropertiesArgsDict",
    "BudgetFilterArgs",
    "BudgetFilterArgsDict",
    "BudgetTimePeriodArgs",
    "BudgetTimePeriodArgsDict",
    "CostAllocationProportionArgs",
    "CostAllocationProportionArgsDict",
    "CostAllocationRuleDetailsArgs",
    "CostAllocationRuleDetailsArgsDict",
    "CostAllocationRulePropertiesArgs",
    "CostAllocationRulePropertiesArgsDict",
    "CustomerMetadataArgs",
    "CustomerMetadataArgsDict",
    "ExportDatasetConfigurationArgs",
    "ExportDatasetConfigurationArgsDict",
    "ExportDatasetArgs",
    "ExportDatasetArgsDict",
    "ExportDefinitionArgs",
    "ExportDefinitionArgsDict",
    "ExportDeliveryDestinationArgs",
    "ExportDeliveryDestinationArgsDict",
    "ExportDeliveryInfoArgs",
    "ExportDeliveryInfoArgsDict",
    "ExportRecurrencePeriodArgs",
    "ExportRecurrencePeriodArgsDict",
    "ExportScheduleArgs",
    "ExportScheduleArgsDict",
    "ExportTimePeriodArgs",
    "ExportTimePeriodArgsDict",
    "FileDestinationArgs",
    "FileDestinationArgsDict",
    "KpiPropertiesArgs",
    "KpiPropertiesArgsDict",
    "NotificationPropertiesArgs",
    "NotificationPropertiesArgsDict",
    "NotificationArgs",
    "NotificationArgsDict",
    "PivotPropertiesArgs",
    "PivotPropertiesArgsDict",
    "ReportAggregationArgs",
    "ReportAggregationArgsDict",
    "ReportComparisonExpressionArgs",
    "ReportComparisonExpressionArgsDict",
    "ReportConfigAggregationArgs",
    "ReportConfigAggregationArgsDict",
    "ReportConfigComparisonExpressionArgs",
    "ReportConfigComparisonExpressionArgsDict",
    "ReportConfigDatasetConfigurationArgs",
    "ReportConfigDatasetConfigurationArgsDict",
    "ReportConfigDatasetArgs",
    "ReportConfigDatasetArgsDict",
    "ReportConfigFilterArgs",
    "ReportConfigFilterArgsDict",
    "ReportConfigGroupingArgs",
    "ReportConfigGroupingArgsDict",
    "ReportConfigSortingArgs",
    "ReportConfigSortingArgsDict",
    "ReportConfigTimePeriodArgs",
    "ReportConfigTimePeriodArgsDict",
    "ReportDatasetConfigurationArgs",
    "ReportDatasetConfigurationArgsDict",
    "ReportDatasetArgs",
    "ReportDatasetArgsDict",
    "ReportDefinitionArgs",
    "ReportDefinitionArgsDict",
    "ReportDeliveryDestinationArgs",
    "ReportDeliveryDestinationArgsDict",
    "ReportDeliveryInfoArgs",
    "ReportDeliveryInfoArgsDict",
    "ReportFilterArgs",
    "ReportFilterArgsDict",
    "ReportGroupingArgs",
    "ReportGroupingArgsDict",
    "ReportRecurrencePeriodArgs",
    "ReportRecurrencePeriodArgsDict",
    "ReportScheduleArgs",
    "ReportScheduleArgsDict",
    "ReportTimePeriodArgs",
    "ReportTimePeriodArgsDict",
    "SchedulePropertiesArgs",
    "SchedulePropertiesArgsDict",
    "SettingsPropertiesCacheArgs",
    "SettingsPropertiesCacheArgsDict",
    "SourceCostAllocationResourceArgs",
    "SourceCostAllocationResourceArgsDict",
    "SystemAssignedServiceIdentityArgs",
    "SystemAssignedServiceIdentityArgsDict",
    "TagInheritancePropertiesArgs",
    "TagInheritancePropertiesArgsDict",
    "TargetCostAllocationResourceArgs",
    "TargetCostAllocationResourceArgsDict",
]

class BudgetComparisonExpressionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, BudgetOperatorType]]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BudgetComparisonExpressionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[Union[_builtins.str, BudgetOperatorType]],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, BudgetOperatorType]]: ...
    @operator.setter
    def operator(
        self, value: pulumi.Input[Union[_builtins.str, BudgetOperatorType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class BudgetFilterPropertiesArgsDict(TypedDict):
    dimensions: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]

@pulumi.input_type
class BudgetFilterPropertiesArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
        tags: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]): ...

class BudgetFilterArgsDict(TypedDict):
    and_: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgsDict]]]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]

@pulumi.input_type
class BudgetFilterArgs:
    def __init__(
        __self__,
        *,
        and_: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgs]]]
        ] = ...,
        dimensions: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
        tags: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgs]]]]: ...
    @and_.setter
    def and_(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]): ...

class BudgetTimePeriodArgsDict(TypedDict):
    start_date: pulumi.Input[_builtins.str]
    end_date: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BudgetTimePeriodArgs:
    def __init__(
        __self__,
        *,
        start_date: pulumi.Input[_builtins.str],
        end_date: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[_builtins.str]: ...
    @start_date.setter
    def start_date(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CostAllocationProportionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    percentage: pulumi.Input[_builtins.float]

@pulumi.input_type
class CostAllocationProportionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        percentage: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> pulumi.Input[_builtins.float]: ...
    @percentage.setter
    def percentage(self, value: pulumi.Input[_builtins.float]): ...

class CostAllocationRuleDetailsArgsDict(TypedDict):
    source_resources: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SourceCostAllocationResourceArgsDict]]]
    ]
    target_resources: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TargetCostAllocationResourceArgsDict]]]
    ]

@pulumi.input_type
class CostAllocationRuleDetailsArgs:
    def __init__(
        __self__,
        *,
        source_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[SourceCostAllocationResourceArgs]]]
        ] = ...,
        target_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetCostAllocationResourceArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceResources")
    def source_resources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SourceCostAllocationResourceArgs]]]
    ]: ...
    @source_resources.setter
    def source_resources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SourceCostAllocationResourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetCostAllocationResourceArgs]]]
    ]: ...
    @target_resources.setter
    def target_resources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetCostAllocationResourceArgs]]]
        ],
    ): ...

class CostAllocationRulePropertiesArgsDict(TypedDict):
    details: pulumi.Input[CostAllocationRuleDetailsArgsDict]
    status: pulumi.Input[Union[_builtins.str, RuleStatus]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CostAllocationRulePropertiesArgs:
    def __init__(
        __self__,
        *,
        details: pulumi.Input[CostAllocationRuleDetailsArgs],
        status: pulumi.Input[Union[_builtins.str, RuleStatus]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> pulumi.Input[CostAllocationRuleDetailsArgs]: ...
    @details.setter
    def details(self, value: pulumi.Input[CostAllocationRuleDetailsArgs]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, RuleStatus]]: ...
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, RuleStatus]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomerMetadataArgsDict(TypedDict):
    billing_account_id: pulumi.Input[_builtins.str]
    billing_profile_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class CustomerMetadataArgs:
    def __init__(
        __self__,
        *,
        billing_account_id: pulumi.Input[_builtins.str],
        billing_profile_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="billingProfileId")
    def billing_profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @billing_profile_id.setter
    def billing_profile_id(self, value: pulumi.Input[_builtins.str]): ...

class ExportDatasetConfigurationArgsDict(TypedDict):
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ExportDatasetConfigurationArgs:
    def __init__(
        __self__,
        *,
        columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ExportDatasetArgsDict(TypedDict):
    configuration: NotRequired[pulumi.Input[ExportDatasetConfigurationArgsDict]]
    granularity: NotRequired[pulumi.Input[Union[_builtins.str, GranularityType]]]

@pulumi.input_type
class ExportDatasetArgs:
    def __init__(
        __self__,
        *,
        configuration: Optional[pulumi.Input[ExportDatasetConfigurationArgs]] = ...,
        granularity: Optional[
            pulumi.Input[Union[_builtins.str, GranularityType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[ExportDatasetConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[ExportDatasetConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def granularity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, GranularityType]]]: ...
    @granularity.setter
    def granularity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, GranularityType]]]
    ): ...

class ExportDefinitionArgsDict(TypedDict):
    timeframe: pulumi.Input[Union[_builtins.str, TimeframeType]]
    type: pulumi.Input[Union[_builtins.str, ExportType]]
    data_set: NotRequired[pulumi.Input[ExportDatasetArgsDict]]
    time_period: NotRequired[pulumi.Input[ExportTimePeriodArgsDict]]

@pulumi.input_type
class ExportDefinitionArgs:
    def __init__(
        __self__,
        *,
        timeframe: pulumi.Input[Union[_builtins.str, TimeframeType]],
        type: pulumi.Input[Union[_builtins.str, ExportType]],
        data_set: Optional[pulumi.Input[ExportDatasetArgs]] = ...,
        time_period: Optional[pulumi.Input[ExportTimePeriodArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def timeframe(self) -> pulumi.Input[Union[_builtins.str, TimeframeType]]: ...
    @timeframe.setter
    def timeframe(self, value: pulumi.Input[Union[_builtins.str, TimeframeType]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ExportType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ExportType]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSet")
    def data_set(self) -> Optional[pulumi.Input[ExportDatasetArgs]]: ...
    @data_set.setter
    def data_set(self, value: Optional[pulumi.Input[ExportDatasetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> Optional[pulumi.Input[ExportTimePeriodArgs]]: ...
    @time_period.setter
    def time_period(self, value: Optional[pulumi.Input[ExportTimePeriodArgs]]): ...

class ExportDeliveryDestinationArgsDict(TypedDict):
    container: pulumi.Input[_builtins.str]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    root_folder_path: NotRequired[pulumi.Input[_builtins.str]]
    sas_token: NotRequired[pulumi.Input[_builtins.str]]
    storage_account: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExportDeliveryDestinationArgs:
    def __init__(
        __self__,
        *,
        container: pulumi.Input[_builtins.str],
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        root_folder_path: Optional[pulumi.Input[_builtins.str]] = ...,
        sas_token: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> pulumi.Input[_builtins.str]: ...
    @container.setter
    def container(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_folder_path.setter
    def root_folder_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sas_token.setter
    def sas_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account.setter
    def storage_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExportDeliveryInfoArgsDict(TypedDict):
    destination: pulumi.Input[ExportDeliveryDestinationArgsDict]

@pulumi.input_type
class ExportDeliveryInfoArgs:
    def __init__(
        __self__, *, destination: pulumi.Input[ExportDeliveryDestinationArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[ExportDeliveryDestinationArgs]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[ExportDeliveryDestinationArgs]): ...

class ExportRecurrencePeriodArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExportRecurrencePeriodArgs:
    def __init__(
        __self__,
        *,
        from_: pulumi.Input[_builtins.str],
        to: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExportScheduleArgsDict(TypedDict):
    recurrence: NotRequired[pulumi.Input[Union[_builtins.str, RecurrenceType]]]
    recurrence_period: NotRequired[pulumi.Input[ExportRecurrencePeriodArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, StatusType]]]

@pulumi.input_type
class ExportScheduleArgs:
    def __init__(
        __self__,
        *,
        recurrence: Optional[pulumi.Input[Union[_builtins.str, RecurrenceType]]] = ...,
        recurrence_period: Optional[pulumi.Input[ExportRecurrencePeriodArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, StatusType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RecurrenceType]]]: ...
    @recurrence.setter
    def recurrence(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RecurrenceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recurrencePeriod")
    def recurrence_period(
        self,
    ) -> Optional[pulumi.Input[ExportRecurrencePeriodArgs]]: ...
    @recurrence_period.setter
    def recurrence_period(
        self, value: Optional[pulumi.Input[ExportRecurrencePeriodArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, StatusType]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StatusType]]]
    ): ...

class ExportTimePeriodArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExportTimePeriodArgs:
    def __init__(
        __self__, *, from_: pulumi.Input[_builtins.str], to: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.str]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.str]): ...

class FileDestinationArgsDict(TypedDict):
    file_formats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FileFormat]]]]
    ]

@pulumi.input_type
class FileDestinationArgs:
    def __init__(
        __self__,
        *,
        file_formats: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FileFormat]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileFormats")
    def file_formats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FileFormat]]]]
    ]: ...
    @file_formats.setter
    def file_formats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FileFormat]]]]
        ],
    ): ...

class KpiPropertiesArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, KpiTypeType]]]

@pulumi.input_type
class KpiPropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, KpiTypeType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, KpiTypeType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, KpiTypeType]]]
    ): ...

class NotificationPropertiesArgsDict(TypedDict):
    subject: pulumi.Input[_builtins.str]
    to: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    language: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    regional_format: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NotificationPropertiesArgs:
    def __init__(
        __self__,
        *,
        subject: pulumi.Input[_builtins.str],
        to: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        language: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]: ...
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @to.setter
    def to(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionalFormat")
    def regional_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_format.setter
    def regional_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NotificationArgsDict(TypedDict):
    contact_emails: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    enabled: pulumi.Input[_builtins.bool]
    operator: pulumi.Input[Union[_builtins.str, BudgetNotificationOperatorType]]
    threshold: pulumi.Input[_builtins.float]
    contact_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    contact_roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    frequency: NotRequired[pulumi.Input[Union[_builtins.str, Frequency]]]
    locale: NotRequired[pulumi.Input[Union[_builtins.str, CultureCode]]]
    threshold_type: NotRequired[pulumi.Input[Union[_builtins.str, ThresholdType]]]

@pulumi.input_type
class NotificationArgs:
    def __init__(
        __self__,
        *,
        contact_emails: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        enabled: pulumi.Input[_builtins.bool],
        operator: pulumi.Input[Union[_builtins.str, BudgetNotificationOperatorType]],
        threshold: pulumi.Input[_builtins.float],
        contact_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        contact_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        frequency: Optional[pulumi.Input[Union[_builtins.str, Frequency]]] = ...,
        locale: Optional[pulumi.Input[Union[_builtins.str, CultureCode]]] = ...,
        threshold_type: Optional[
            pulumi.Input[Union[_builtins.str, ThresholdType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactEmails")
    def contact_emails(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @contact_emails.setter
    def contact_emails(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def operator(
        self,
    ) -> pulumi.Input[Union[_builtins.str, BudgetNotificationOperatorType]]: ...
    @operator.setter
    def operator(
        self, value: pulumi.Input[Union[_builtins.str, BudgetNotificationOperatorType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.float]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="contactGroups")
    def contact_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @contact_groups.setter
    def contact_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contactRoles")
    def contact_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @contact_roles.setter
    def contact_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[Union[_builtins.str, Frequency]]]: ...
    @frequency.setter
    def frequency(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Frequency]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[Union[_builtins.str, CultureCode]]]: ...
    @locale.setter
    def locale(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CultureCode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thresholdType")
    def threshold_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ThresholdType]]]: ...
    @threshold_type.setter
    def threshold_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ThresholdType]]]
    ): ...

class PivotPropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, PivotTypeType]]]

@pulumi.input_type
class PivotPropertiesArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, PivotTypeType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, PivotTypeType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PivotTypeType]]]
    ): ...

class ReportAggregationArgsDict(TypedDict):
    function: pulumi.Input[Union[_builtins.str, FunctionType]]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReportAggregationArgs:
    def __init__(
        __self__,
        *,
        function: pulumi.Input[Union[_builtins.str, FunctionType]],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> pulumi.Input[Union[_builtins.str, FunctionType]]: ...
    @function.setter
    def function(self, value: pulumi.Input[Union[_builtins.str, FunctionType]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ReportComparisonExpressionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, OperatorType]]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ReportComparisonExpressionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[Union[_builtins.str, OperatorType]],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, OperatorType]]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, OperatorType]]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ReportConfigAggregationArgsDict(TypedDict):
    function: pulumi.Input[Union[_builtins.str, FunctionType]]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReportConfigAggregationArgs:
    def __init__(
        __self__,
        *,
        function: pulumi.Input[Union[_builtins.str, FunctionType]],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> pulumi.Input[Union[_builtins.str, FunctionType]]: ...
    @function.setter
    def function(self, value: pulumi.Input[Union[_builtins.str, FunctionType]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ReportConfigComparisonExpressionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, OperatorType]]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ReportConfigComparisonExpressionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[Union[_builtins.str, OperatorType]],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, OperatorType]]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, OperatorType]]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ReportConfigDatasetConfigurationArgsDict(TypedDict):
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ReportConfigDatasetConfigurationArgs:
    def __init__(
        __self__,
        *,
        columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ReportConfigDatasetArgsDict(TypedDict):
    aggregation: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ReportConfigAggregationArgsDict]]]
    ]
    configuration: NotRequired[pulumi.Input[ReportConfigDatasetConfigurationArgsDict]]
    filter: NotRequired[pulumi.Input[ReportConfigFilterArgsDict]]
    granularity: NotRequired[pulumi.Input[Union[_builtins.str, ReportGranularityType]]]
    grouping: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ReportConfigGroupingArgsDict]]]
    ]
    sorting: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ReportConfigSortingArgsDict]]]
    ]

@pulumi.input_type
class ReportConfigDatasetArgs:
    def __init__(
        __self__,
        *,
        aggregation: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReportConfigAggregationArgs]]]
        ] = ...,
        configuration: Optional[
            pulumi.Input[ReportConfigDatasetConfigurationArgs]
        ] = ...,
        filter: Optional[pulumi.Input[ReportConfigFilterArgs]] = ...,
        granularity: Optional[
            pulumi.Input[Union[_builtins.str, ReportGranularityType]]
        ] = ...,
        grouping: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReportConfigGroupingArgs]]]
        ] = ...,
        sorting: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReportConfigSortingArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aggregation(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ReportConfigAggregationArgs]]]
    ]: ...
    @aggregation.setter
    def aggregation(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReportConfigAggregationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[ReportConfigDatasetConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[ReportConfigDatasetConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[ReportConfigFilterArgs]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[ReportConfigFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def granularity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ReportGranularityType]]]: ...
    @granularity.setter
    def granularity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ReportGranularityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def grouping(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigGroupingArgs]]]]: ...
    @grouping.setter
    def grouping(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigGroupingArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sorting(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigSortingArgs]]]]: ...
    @sorting.setter
    def sorting(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigSortingArgs]]]],
    ): ...

class ReportConfigFilterArgsDict(TypedDict):
    and_: NotRequired[pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgsDict]]]]
    dimensions: NotRequired[pulumi.Input[ReportConfigComparisonExpressionArgsDict]]
    or_: NotRequired[pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgsDict]]]]
    tags: NotRequired[pulumi.Input[ReportConfigComparisonExpressionArgsDict]]

@pulumi.input_type
class ReportConfigFilterArgs:
    def __init__(
        __self__,
        *,
        and_: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgs]]]
        ] = ...,
        dimensions: Optional[pulumi.Input[ReportConfigComparisonExpressionArgs]] = ...,
        or_: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[ReportConfigComparisonExpressionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgs]]]]: ...
    @and_.setter
    def and_(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[ReportConfigComparisonExpressionArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[ReportConfigComparisonExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="or")
    def or_(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgs]]]]: ...
    @or_.setter
    def or_(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReportConfigFilterArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[ReportConfigComparisonExpressionArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[ReportConfigComparisonExpressionArgs]]
    ): ...

class ReportConfigGroupingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, QueryColumnType]]

@pulumi.input_type
class ReportConfigGroupingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, QueryColumnType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, QueryColumnType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, QueryColumnType]]): ...

class ReportConfigSortingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    direction: NotRequired[pulumi.Input[Union[_builtins.str, ReportConfigSortingType]]]

@pulumi.input_type
class ReportConfigSortingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        direction: Optional[
            pulumi.Input[Union[_builtins.str, ReportConfigSortingType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def direction(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ReportConfigSortingType]]]: ...
    @direction.setter
    def direction(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ReportConfigSortingType]]],
    ): ...

class ReportConfigTimePeriodArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReportConfigTimePeriodArgs:
    def __init__(
        __self__, *, from_: pulumi.Input[_builtins.str], to: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.str]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.str]): ...

class ReportDatasetConfigurationArgsDict(TypedDict):
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ReportDatasetConfigurationArgs:
    def __init__(
        __self__,
        *,
        columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ReportDatasetArgsDict(TypedDict):
    aggregation: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ReportAggregationArgsDict]]]
    ]
    configuration: NotRequired[pulumi.Input[ReportDatasetConfigurationArgsDict]]
    filter: NotRequired[pulumi.Input[ReportFilterArgsDict]]
    granularity: NotRequired[pulumi.Input[Union[_builtins.str, GranularityType]]]
    grouping: NotRequired[pulumi.Input[Sequence[pulumi.Input[ReportGroupingArgsDict]]]]

@pulumi.input_type
class ReportDatasetArgs:
    def __init__(
        __self__,
        *,
        aggregation: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReportAggregationArgs]]]
        ] = ...,
        configuration: Optional[pulumi.Input[ReportDatasetConfigurationArgs]] = ...,
        filter: Optional[pulumi.Input[ReportFilterArgs]] = ...,
        granularity: Optional[
            pulumi.Input[Union[_builtins.str, GranularityType]]
        ] = ...,
        grouping: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReportGroupingArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aggregation(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[ReportAggregationArgs]]]]: ...
    @aggregation.setter
    def aggregation(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ReportAggregationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[ReportDatasetConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[ReportDatasetConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[ReportFilterArgs]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[ReportFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def granularity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, GranularityType]]]: ...
    @granularity.setter
    def granularity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, GranularityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def grouping(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReportGroupingArgs]]]]: ...
    @grouping.setter
    def grouping(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReportGroupingArgs]]]]
    ): ...

class ReportDefinitionArgsDict(TypedDict):
    timeframe: pulumi.Input[Union[_builtins.str, TimeframeType]]
    type: pulumi.Input[Union[_builtins.str, ReportType]]
    dataset: NotRequired[pulumi.Input[ReportDatasetArgsDict]]
    time_period: NotRequired[pulumi.Input[ReportTimePeriodArgsDict]]

@pulumi.input_type
class ReportDefinitionArgs:
    def __init__(
        __self__,
        *,
        timeframe: pulumi.Input[Union[_builtins.str, TimeframeType]],
        type: pulumi.Input[Union[_builtins.str, ReportType]],
        dataset: Optional[pulumi.Input[ReportDatasetArgs]] = ...,
        time_period: Optional[pulumi.Input[ReportTimePeriodArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def timeframe(self) -> pulumi.Input[Union[_builtins.str, TimeframeType]]: ...
    @timeframe.setter
    def timeframe(self, value: pulumi.Input[Union[_builtins.str, TimeframeType]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ReportType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ReportType]]): ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[ReportDatasetArgs]]: ...
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[ReportDatasetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> Optional[pulumi.Input[ReportTimePeriodArgs]]: ...
    @time_period.setter
    def time_period(self, value: Optional[pulumi.Input[ReportTimePeriodArgs]]): ...

class ReportDeliveryDestinationArgsDict(TypedDict):
    container: pulumi.Input[_builtins.str]
    resource_id: pulumi.Input[_builtins.str]
    root_folder_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReportDeliveryDestinationArgs:
    def __init__(
        __self__,
        *,
        container: pulumi.Input[_builtins.str],
        resource_id: pulumi.Input[_builtins.str],
        root_folder_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> pulumi.Input[_builtins.str]: ...
    @container.setter
    def container(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_folder_path.setter
    def root_folder_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReportDeliveryInfoArgsDict(TypedDict):
    destination: pulumi.Input[ReportDeliveryDestinationArgsDict]

@pulumi.input_type
class ReportDeliveryInfoArgs:
    def __init__(
        __self__, *, destination: pulumi.Input[ReportDeliveryDestinationArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[ReportDeliveryDestinationArgs]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[ReportDeliveryDestinationArgs]): ...

class ReportFilterArgsDict(TypedDict):
    and_: NotRequired[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgsDict]]]]
    dimension: NotRequired[pulumi.Input[ReportComparisonExpressionArgsDict]]
    not_: NotRequired[pulumi.Input[ReportFilterArgsDict]]
    or_: NotRequired[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgsDict]]]]
    tag: NotRequired[pulumi.Input[ReportComparisonExpressionArgsDict]]

@pulumi.input_type
class ReportFilterArgs:
    def __init__(
        __self__,
        *,
        and_: Optional[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgs]]]] = ...,
        dimension: Optional[pulumi.Input[ReportComparisonExpressionArgs]] = ...,
        not_: Optional[pulumi.Input[ReportFilterArgs]] = ...,
        or_: Optional[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgs]]]] = ...,
        tag: Optional[pulumi.Input[ReportComparisonExpressionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgs]]]]: ...
    @and_.setter
    def and_(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[ReportComparisonExpressionArgs]]: ...
    @dimension.setter
    def dimension(
        self, value: Optional[pulumi.Input[ReportComparisonExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[ReportFilterArgs]]: ...
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[ReportFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="or")
    def or_(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgs]]]]: ...
    @or_.setter
    def or_(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReportFilterArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[ReportComparisonExpressionArgs]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[ReportComparisonExpressionArgs]]): ...

class ReportGroupingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, ReportColumnType]]

@pulumi.input_type
class ReportGroupingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, ReportColumnType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ReportColumnType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ReportColumnType]]): ...

class ReportRecurrencePeriodArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReportRecurrencePeriodArgs:
    def __init__(
        __self__,
        *,
        from_: pulumi.Input[_builtins.str],
        to: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReportScheduleArgsDict(TypedDict):
    recurrence: pulumi.Input[Union[_builtins.str, RecurrenceType]]
    recurrence_period: NotRequired[pulumi.Input[ReportRecurrencePeriodArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, StatusType]]]

@pulumi.input_type
class ReportScheduleArgs:
    def __init__(
        __self__,
        *,
        recurrence: pulumi.Input[Union[_builtins.str, RecurrenceType]],
        recurrence_period: Optional[pulumi.Input[ReportRecurrencePeriodArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, StatusType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> pulumi.Input[Union[_builtins.str, RecurrenceType]]: ...
    @recurrence.setter
    def recurrence(self, value: pulumi.Input[Union[_builtins.str, RecurrenceType]]): ...
    @_builtins.property
    @pulumi.getter(name="recurrencePeriod")
    def recurrence_period(
        self,
    ) -> Optional[pulumi.Input[ReportRecurrencePeriodArgs]]: ...
    @recurrence_period.setter
    def recurrence_period(
        self, value: Optional[pulumi.Input[ReportRecurrencePeriodArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, StatusType]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StatusType]]]
    ): ...

class ReportTimePeriodArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReportTimePeriodArgs:
    def __init__(
        __self__, *, from_: pulumi.Input[_builtins.str], to: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.str]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.str]): ...

class SchedulePropertiesArgsDict(TypedDict):
    end_date: pulumi.Input[_builtins.str]
    frequency: pulumi.Input[Union[_builtins.str, ScheduleFrequency]]
    start_date: pulumi.Input[_builtins.str]
    day_of_month: NotRequired[pulumi.Input[_builtins.int]]
    days_of_week: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
    ]
    hour_of_day: NotRequired[pulumi.Input[_builtins.int]]
    weeks_of_month: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeeksOfMonth]]]]
    ]

@pulumi.input_type
class SchedulePropertiesArgs:
    def __init__(
        __self__,
        *,
        end_date: pulumi.Input[_builtins.str],
        frequency: pulumi.Input[Union[_builtins.str, ScheduleFrequency]],
        start_date: pulumi.Input[_builtins.str],
        day_of_month: Optional[pulumi.Input[_builtins.int]] = ...,
        days_of_week: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
        ] = ...,
        hour_of_day: Optional[pulumi.Input[_builtins.int]] = ...,
        weeks_of_month: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeeksOfMonth]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Input[_builtins.str]: ...
    @end_date.setter
    def end_date(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[Union[_builtins.str, ScheduleFrequency]]: ...
    @frequency.setter
    def frequency(
        self, value: pulumi.Input[Union[_builtins.str, ScheduleFrequency]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[_builtins.str]: ...
    @start_date.setter
    def start_date(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day_of_month.setter
    def day_of_month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
    ]: ...
    @days_of_week.setter
    def days_of_week(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DaysOfWeek]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonth")
    def weeks_of_month(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeeksOfMonth]]]]
    ]: ...
    @weeks_of_month.setter
    def weeks_of_month(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeeksOfMonth]]]]
        ],
    ): ...

class SettingsPropertiesCacheArgsDict(TypedDict):
    channel: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    subchannel: pulumi.Input[_builtins.str]
    parent: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SettingsPropertiesCacheArgs:
    def __init__(
        __self__,
        *,
        channel: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        subchannel: pulumi.Input[_builtins.str],
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Input[_builtins.str]: ...
    @channel.setter
    def channel(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subchannel(self) -> pulumi.Input[_builtins.str]: ...
    @subchannel.setter
    def subchannel(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SourceCostAllocationResourceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    resource_type: pulumi.Input[Union[_builtins.str, CostAllocationResourceType]]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class SourceCostAllocationResourceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        resource_type: pulumi.Input[Union[_builtins.str, CostAllocationResourceType]],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CostAllocationResourceType]]: ...
    @resource_type.setter
    def resource_type(
        self, value: pulumi.Input[Union[_builtins.str, CostAllocationResourceType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class SystemAssignedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]]

@pulumi.input_type
class SystemAssignedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]]: ...
    @type.setter
    def type(
        self,
        value: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]],
    ): ...

class TagInheritancePropertiesArgsDict(TypedDict):
    prefer_container_tags: pulumi.Input[_builtins.bool]

@pulumi.input_type
class TagInheritancePropertiesArgs:
    def __init__(
        __self__, *, prefer_container_tags: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferContainerTags")
    def prefer_container_tags(self) -> pulumi.Input[_builtins.bool]: ...
    @prefer_container_tags.setter
    def prefer_container_tags(self, value: pulumi.Input[_builtins.bool]): ...

class TargetCostAllocationResourceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    policy_type: pulumi.Input[Union[_builtins.str, CostAllocationPolicyType]]
    resource_type: pulumi.Input[Union[_builtins.str, CostAllocationResourceType]]
    values: pulumi.Input[Sequence[pulumi.Input[CostAllocationProportionArgsDict]]]

@pulumi.input_type
class TargetCostAllocationResourceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        policy_type: pulumi.Input[Union[_builtins.str, CostAllocationPolicyType]],
        resource_type: pulumi.Input[Union[_builtins.str, CostAllocationResourceType]],
        values: pulumi.Input[Sequence[pulumi.Input[CostAllocationProportionArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CostAllocationPolicyType]]: ...
    @policy_type.setter
    def policy_type(
        self, value: pulumi.Input[Union[_builtins.str, CostAllocationPolicyType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CostAllocationResourceType]]: ...
    @resource_type.setter
    def resource_type(
        self, value: pulumi.Input[Union[_builtins.str, CostAllocationResourceType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[CostAllocationProportionArgs]]]: ...
    @values.setter
    def values(
        self, value: pulumi.Input[Sequence[pulumi.Input[CostAllocationProportionArgs]]]
    ): ...

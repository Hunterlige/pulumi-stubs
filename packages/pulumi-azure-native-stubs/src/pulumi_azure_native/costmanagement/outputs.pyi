import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BudgetComparisonExpressionResponse",
    "BudgetFilterPropertiesResponse",
    "BudgetFilterResponse",
    "BudgetTimePeriodResponse",
    "CommonExportPropertiesResponse",
    "ConnectorCollectionErrorInfoResponse",
    "ConnectorCollectionErrorInfoResponseV1",
    "ConnectorCollectionInfoResponse",
    "ConnectorCollectionInfoResponseV1",
    "CostAllocationProportionResponse",
    "CostAllocationRuleDetailsResponse",
    "CostAllocationRulePropertiesResponse",
    "CurrentSpendResponse",
    "CustomerMetadataResponse",
    "ErrorDetailsResponse",
    "ExportDatasetConfigurationResponse",
    "ExportDatasetResponse",
    "ExportDefinitionResponse",
    "ExportDeliveryDestinationResponse",
    "ExportDeliveryInfoResponse",
    "ExportExecutionListResultResponse",
    "ExportRecurrencePeriodResponse",
    "ExportRunResponse",
    "ExportScheduleResponse",
    "ExportTimePeriodResponse",
    "FileDestinationResponse",
    "ForecastSpendResponse",
    "KpiPropertiesResponse",
    "NotificationPropertiesResponse",
    "NotificationResponse",
    "PivotPropertiesResponse",
    "ReportAggregationResponse",
    "ReportComparisonExpressionResponse",
    "ReportConfigAggregationResponse",
    "ReportConfigComparisonExpressionResponse",
    "ReportConfigDatasetConfigurationResponse",
    "ReportConfigDatasetResponse",
    "ReportConfigFilterResponse",
    "ReportConfigGroupingResponse",
    "ReportConfigSortingResponse",
    "ReportConfigTimePeriodResponse",
    "ReportDatasetConfigurationResponse",
    "ReportDatasetResponse",
    "ReportDefinitionResponse",
    "ReportDeliveryDestinationResponse",
    "ReportDeliveryInfoResponse",
    "ReportFilterResponse",
    "ReportGroupingResponse",
    "ReportRecurrencePeriodResponse",
    "ReportScheduleResponse",
    "ReportTimePeriodResponse",
    "SchedulePropertiesResponse",
    "SettingsPropertiesResponseCache",
    "SourceCostAllocationResourceResponse",
    "SystemAssignedServiceIdentityResponse",
    "SystemDataResponse",
    "TagInheritancePropertiesResponse",
    "TargetCostAllocationResourceResponse",
]

@pulumi.output_type
class BudgetComparisonExpressionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class BudgetFilterPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        dimensions: Optional[outputs.BudgetComparisonExpressionResponse] = ...,
        tags: Optional[outputs.BudgetComparisonExpressionResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetComparisonExpressionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetComparisonExpressionResponse]: ...

@pulumi.output_type
class BudgetFilterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        and_: Optional[Sequence[outputs.BudgetFilterPropertiesResponse]] = ...,
        dimensions: Optional[outputs.BudgetComparisonExpressionResponse] = ...,
        tags: Optional[outputs.BudgetComparisonExpressionResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[Sequence[outputs.BudgetFilterPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetComparisonExpressionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetComparisonExpressionResponse]: ...

@pulumi.output_type
class BudgetTimePeriodResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, start_date: _builtins.str, end_date: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CommonExportPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        definition: outputs.ExportDefinitionResponse,
        delivery_info: outputs.ExportDeliveryInfoResponse,
        next_run_time_estimate: _builtins.str,
        format: Optional[_builtins.str] = ...,
        partition_data: Optional[_builtins.bool] = ...,
        run_history: Optional[outputs.ExportExecutionListResultResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> outputs.ExportDefinitionResponse: ...
    @_builtins.property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> outputs.ExportDeliveryInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="nextRunTimeEstimate")
    def next_run_time_estimate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionData")
    def partition_data(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runHistory")
    def run_history(self) -> Optional[outputs.ExportExecutionListResultResponse]: ...

@pulumi.output_type
class ConnectorCollectionErrorInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_code: _builtins.str,
        error_inner_message: _builtins.str,
        error_message: _builtins.str,
        error_start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorInnerMessage")
    def error_inner_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorStartTime")
    def error_start_time(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorCollectionErrorInfoResponseV1(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_code: _builtins.str,
        error_message: _builtins.str,
        error_start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorStartTime")
    def error_start_time(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorCollectionInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_checked: _builtins.str,
        last_updated: _builtins.str,
        source_last_updated: _builtins.str,
        error: Optional[outputs.ConnectorCollectionErrorInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceLastUpdated")
    def source_last_updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ConnectorCollectionErrorInfoResponse]: ...

@pulumi.output_type
class ConnectorCollectionInfoResponseV1(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_run: _builtins.str,
        last_updated: _builtins.str,
        source_last_updated: _builtins.str,
        error: Optional[outputs.ConnectorCollectionErrorInfoResponseV1] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastRun")
    def last_run(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceLastUpdated")
    def source_last_updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ConnectorCollectionErrorInfoResponseV1]: ...

@pulumi.output_type
class CostAllocationProportionResponse(dict):
    def __init__(
        __self__, *, name: _builtins.str, percentage: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> _builtins.float: ...

@pulumi.output_type
class CostAllocationRuleDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_resources: Optional[
            Sequence[outputs.SourceCostAllocationResourceResponse]
        ] = ...,
        target_resources: Optional[
            Sequence[outputs.TargetCostAllocationResourceResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceResources")
    def source_resources(
        self,
    ) -> Optional[Sequence[outputs.SourceCostAllocationResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(
        self,
    ) -> Optional[Sequence[outputs.TargetCostAllocationResourceResponse]]: ...

@pulumi.output_type
class CostAllocationRulePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_date: _builtins.str,
        details: outputs.CostAllocationRuleDetailsResponse,
        status: _builtins.str,
        updated_date: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> outputs.CostAllocationRuleDetailsResponse: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedDate")
    def updated_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CurrentSpendResponse(dict):
    def __init__(__self__, *, amount: _builtins.float, unit: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...

@pulumi.output_type
class CustomerMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        billing_account_id: _builtins.str,
        billing_profile_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileId")
    def billing_profile_id(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDetailsResponse(dict):
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class ExportDatasetConfigurationResponse(dict):
    def __init__(
        __self__, *, columns: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ExportDatasetResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[outputs.ExportDatasetConfigurationResponse] = ...,
        granularity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[outputs.ExportDatasetConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def granularity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        timeframe: _builtins.str,
        type: _builtins.str,
        data_set: Optional[outputs.ExportDatasetResponse] = ...,
        time_period: Optional[outputs.ExportTimePeriodResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def timeframe(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSet")
    def data_set(self) -> Optional[outputs.ExportDatasetResponse]: ...
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> Optional[outputs.ExportTimePeriodResponse]: ...

@pulumi.output_type
class ExportDeliveryDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container: _builtins.str,
        resource_id: Optional[_builtins.str] = ...,
        root_folder_path: Optional[_builtins.str] = ...,
        sas_token: Optional[_builtins.str] = ...,
        storage_account: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportDeliveryInfoResponse(dict):
    def __init__(
        __self__, *, destination: outputs.ExportDeliveryDestinationResponse
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.ExportDeliveryDestinationResponse: ...

@pulumi.output_type
class ExportExecutionListResultResponse(dict):
    def __init__(__self__, *, value: Sequence[outputs.ExportRunResponse]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ExportRunResponse]: ...

@pulumi.output_type
class ExportRecurrencePeriodResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, from_: _builtins.str, to: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportRunResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        e_tag: Optional[_builtins.str] = ...,
        error: Optional[outputs.ErrorDetailsResponse] = ...,
        execution_type: Optional[_builtins.str] = ...,
        file_name: Optional[_builtins.str] = ...,
        processing_end_time: Optional[_builtins.str] = ...,
        processing_start_time: Optional[_builtins.str] = ...,
        run_settings: Optional[outputs.CommonExportPropertiesResponse] = ...,
        status: Optional[_builtins.str] = ...,
        submitted_by: Optional[_builtins.str] = ...,
        submitted_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingEndTime")
    def processing_end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingStartTime")
    def processing_start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runSettings")
    def run_settings(self) -> Optional[outputs.CommonExportPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="submittedBy")
    def submitted_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="submittedTime")
    def submitted_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recurrence: Optional[_builtins.str] = ...,
        recurrence_period: Optional[outputs.ExportRecurrencePeriodResponse] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recurrencePeriod")
    def recurrence_period(self) -> Optional[outputs.ExportRecurrencePeriodResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportTimePeriodResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, from_: _builtins.str, to: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.str: ...

@pulumi.output_type
class FileDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, file_formats: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileFormats")
    def file_formats(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ForecastSpendResponse(dict):
    def __init__(__self__, *, amount: _builtins.float, unit: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...

@pulumi.output_type
class KpiPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        id: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subject: _builtins.str,
        to: Sequence[_builtins.str],
        language: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        regional_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionalFormat")
    def regional_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        contact_emails: Sequence[_builtins.str],
        enabled: _builtins.bool,
        operator: _builtins.str,
        threshold: _builtins.float,
        contact_groups: Optional[Sequence[_builtins.str]] = ...,
        contact_roles: Optional[Sequence[_builtins.str]] = ...,
        frequency: Optional[_builtins.str] = ...,
        locale: Optional[_builtins.str] = ...,
        threshold_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactEmails")
    def contact_emails(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="contactGroups")
    def contact_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contactRoles")
    def contact_roles(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thresholdType")
    def threshold_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PivotPropertiesResponse(dict):
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
class ReportAggregationResponse(dict):
    def __init__(__self__, *, function: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ReportComparisonExpressionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ReportConfigAggregationResponse(dict):
    def __init__(__self__, *, function: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ReportConfigComparisonExpressionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ReportConfigDatasetConfigurationResponse(dict):
    def __init__(
        __self__, *, columns: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ReportConfigDatasetResponse(dict):
    def __init__(
        __self__,
        *,
        aggregation: Optional[
            Mapping[str, outputs.ReportConfigAggregationResponse]
        ] = ...,
        configuration: Optional[outputs.ReportConfigDatasetConfigurationResponse] = ...,
        filter: Optional[outputs.ReportConfigFilterResponse] = ...,
        granularity: Optional[_builtins.str] = ...,
        grouping: Optional[Sequence[outputs.ReportConfigGroupingResponse]] = ...,
        sorting: Optional[Sequence[outputs.ReportConfigSortingResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aggregation(
        self,
    ) -> Optional[Mapping[str, outputs.ReportConfigAggregationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.ReportConfigDatasetConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.ReportConfigFilterResponse]: ...
    @_builtins.property
    @pulumi.getter
    def granularity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def grouping(self) -> Optional[Sequence[outputs.ReportConfigGroupingResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sorting(self) -> Optional[Sequence[outputs.ReportConfigSortingResponse]]: ...

@pulumi.output_type
class ReportConfigFilterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        and_: Optional[Sequence[outputs.ReportConfigFilterResponse]] = ...,
        dimensions: Optional[outputs.ReportConfigComparisonExpressionResponse] = ...,
        or_: Optional[Sequence[outputs.ReportConfigFilterResponse]] = ...,
        tags: Optional[outputs.ReportConfigComparisonExpressionResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[Sequence[outputs.ReportConfigFilterResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[outputs.ReportConfigComparisonExpressionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="or")
    def or_(self) -> Optional[Sequence[outputs.ReportConfigFilterResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.ReportConfigComparisonExpressionResponse]: ...

@pulumi.output_type
class ReportConfigGroupingResponse(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ReportConfigSortingResponse(dict):
    def __init__(
        __self__, *, name: _builtins.str, direction: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReportConfigTimePeriodResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, from_: _builtins.str, to: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.str: ...

@pulumi.output_type
class ReportDatasetConfigurationResponse(dict):
    def __init__(
        __self__, *, columns: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ReportDatasetResponse(dict):
    def __init__(
        __self__,
        *,
        aggregation: Optional[Mapping[str, outputs.ReportAggregationResponse]] = ...,
        configuration: Optional[outputs.ReportDatasetConfigurationResponse] = ...,
        filter: Optional[outputs.ReportFilterResponse] = ...,
        granularity: Optional[_builtins.str] = ...,
        grouping: Optional[Sequence[outputs.ReportGroupingResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aggregation(
        self,
    ) -> Optional[Mapping[str, outputs.ReportAggregationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[outputs.ReportDatasetConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.ReportFilterResponse]: ...
    @_builtins.property
    @pulumi.getter
    def granularity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def grouping(self) -> Optional[Sequence[outputs.ReportGroupingResponse]]: ...

@pulumi.output_type
class ReportDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        timeframe: _builtins.str,
        type: _builtins.str,
        dataset: Optional[outputs.ReportDatasetResponse] = ...,
        time_period: Optional[outputs.ReportTimePeriodResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def timeframe(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[outputs.ReportDatasetResponse]: ...
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> Optional[outputs.ReportTimePeriodResponse]: ...

@pulumi.output_type
class ReportDeliveryDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container: _builtins.str,
        resource_id: _builtins.str,
        root_folder_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReportDeliveryInfoResponse(dict):
    def __init__(
        __self__, *, destination: outputs.ReportDeliveryDestinationResponse
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.ReportDeliveryDestinationResponse: ...

@pulumi.output_type
class ReportFilterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        and_: Optional[Sequence[outputs.ReportFilterResponse]] = ...,
        dimension: Optional[outputs.ReportComparisonExpressionResponse] = ...,
        not_: Optional[outputs.ReportFilterResponse] = ...,
        or_: Optional[Sequence[outputs.ReportFilterResponse]] = ...,
        tag: Optional[outputs.ReportComparisonExpressionResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[Sequence[outputs.ReportFilterResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.ReportComparisonExpressionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.ReportFilterResponse]: ...
    @_builtins.property
    @pulumi.getter(name="or")
    def or_(self) -> Optional[Sequence[outputs.ReportFilterResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[outputs.ReportComparisonExpressionResponse]: ...

@pulumi.output_type
class ReportGroupingResponse(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ReportRecurrencePeriodResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, from_: _builtins.str, to: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReportScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recurrence: _builtins.str,
        recurrence_period: Optional[outputs.ReportRecurrencePeriodResponse] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recurrencePeriod")
    def recurrence_period(self) -> Optional[outputs.ReportRecurrencePeriodResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReportTimePeriodResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, from_: _builtins.str, to: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.str: ...

@pulumi.output_type
class SchedulePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_date: _builtins.str,
        frequency: _builtins.str,
        start_date: _builtins.str,
        day_of_month: Optional[_builtins.int] = ...,
        days_of_week: Optional[Sequence[_builtins.str]] = ...,
        hour_of_day: Optional[_builtins.int] = ...,
        weeks_of_month: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonth")
    def weeks_of_month(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SettingsPropertiesResponseCache(dict):
    def __init__(
        __self__,
        *,
        channel: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        subchannel: _builtins.str,
        parent: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subchannel(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SourceCostAllocationResourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        resource_type: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class SystemAssignedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TagInheritancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, prefer_container_tags: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferContainerTags")
    def prefer_container_tags(self) -> _builtins.bool: ...

@pulumi.output_type
class TargetCostAllocationResourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        policy_type: _builtins.str,
        resource_type: _builtins.str,
        values: Sequence[outputs.CostAllocationProportionResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[outputs.CostAllocationProportionResponse]: ...

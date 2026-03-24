import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountIamBindingCondition",
    "AccountIamMemberCondition",
    "BudgetAllUpdatesRule",
    "BudgetAmount",
    "BudgetAmountSpecifiedAmount",
    "BudgetBudgetFilter",
    "BudgetBudgetFilterCustomPeriod",
    "BudgetBudgetFilterCustomPeriodEndDate",
    "BudgetBudgetFilterCustomPeriodStartDate",
    "BudgetThresholdRule",
]

@pulumi.output_type
class AccountIamBindingCondition(dict):
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
class AccountIamMemberCondition(dict):
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
class BudgetAllUpdatesRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_default_iam_recipients: Optional[_builtins.bool] = ...,
        enable_project_level_recipients: Optional[_builtins.bool] = ...,
        monitoring_notification_channels: Optional[Sequence[_builtins.str]] = ...,
        pubsub_topic: Optional[_builtins.str] = ...,
        schema_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableDefaultIamRecipients")
    def disable_default_iam_recipients(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableProjectLevelRecipients")
    def enable_project_level_recipients(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringNotificationChannels")
    def monitoring_notification_channels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BudgetAmount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_period_amount: Optional[_builtins.bool] = ...,
        specified_amount: Optional[outputs.BudgetAmountSpecifiedAmount] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastPeriodAmount")
    def last_period_amount(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="specifiedAmount")
    def specified_amount(self) -> Optional[outputs.BudgetAmountSpecifiedAmount]: ...

@pulumi.output_type
class BudgetAmountSpecifiedAmount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        currency_code: Optional[_builtins.str] = ...,
        nanos: Optional[_builtins.int] = ...,
        units: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def units(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BudgetBudgetFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        calendar_period: Optional[_builtins.str] = ...,
        credit_types: Optional[Sequence[_builtins.str]] = ...,
        credit_types_treatment: Optional[_builtins.str] = ...,
        custom_period: Optional[outputs.BudgetBudgetFilterCustomPeriod] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        projects: Optional[Sequence[_builtins.str]] = ...,
        resource_ancestors: Optional[Sequence[_builtins.str]] = ...,
        services: Optional[Sequence[_builtins.str]] = ...,
        subaccounts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="calendarPeriod")
    def calendar_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creditTypes")
    def credit_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="creditTypesTreatment")
    def credit_types_treatment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customPeriod")
    def custom_period(self) -> Optional[outputs.BudgetBudgetFilterCustomPeriod]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def projects(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceAncestors")
    def resource_ancestors(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def services(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def subaccounts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class BudgetBudgetFilterCustomPeriod(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        start_date: outputs.BudgetBudgetFilterCustomPeriodStartDate,
        end_date: Optional[outputs.BudgetBudgetFilterCustomPeriodEndDate] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> outputs.BudgetBudgetFilterCustomPeriodStartDate: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[outputs.BudgetBudgetFilterCustomPeriodEndDate]: ...

@pulumi.output_type
class BudgetBudgetFilterCustomPeriodEndDate(dict):
    def __init__(
        __self__, *, day: _builtins.int, month: _builtins.int, year: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> _builtins.int: ...

@pulumi.output_type
class BudgetBudgetFilterCustomPeriodStartDate(dict):
    def __init__(
        __self__, *, day: _builtins.int, month: _builtins.int, year: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> _builtins.int: ...

@pulumi.output_type
class BudgetThresholdRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        threshold_percent: _builtins.float,
        spend_basis: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="thresholdPercent")
    def threshold_percent(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="spendBasis")
    def spend_basis(self) -> Optional[_builtins.str]: ...

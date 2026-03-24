import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountIamBindingConditionArgs",
    "AccountIamBindingConditionArgsDict",
    "AccountIamMemberConditionArgs",
    "AccountIamMemberConditionArgsDict",
    "BudgetAllUpdatesRuleArgs",
    "BudgetAllUpdatesRuleArgsDict",
    "BudgetAmountArgs",
    "BudgetAmountArgsDict",
    "BudgetAmountSpecifiedAmountArgs",
    "BudgetAmountSpecifiedAmountArgsDict",
    "BudgetBudgetFilterArgs",
    "BudgetBudgetFilterArgsDict",
    "BudgetBudgetFilterCustomPeriodArgs",
    "BudgetBudgetFilterCustomPeriodArgsDict",
    "BudgetBudgetFilterCustomPeriodEndDateArgs",
    "BudgetBudgetFilterCustomPeriodEndDateArgsDict",
    "BudgetBudgetFilterCustomPeriodStartDateArgs",
    "BudgetBudgetFilterCustomPeriodStartDateArgsDict",
    "BudgetThresholdRuleArgs",
    "BudgetThresholdRuleArgsDict",
]

class AccountIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AccountIamBindingConditionArgs:
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

class AccountIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AccountIamMemberConditionArgs:
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

class BudgetAllUpdatesRuleArgsDict(TypedDict):
    disable_default_iam_recipients: NotRequired[pulumi.Input[_builtins.bool]]
    enable_project_level_recipients: NotRequired[pulumi.Input[_builtins.bool]]
    monitoring_notification_channels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    pubsub_topic: NotRequired[pulumi.Input[_builtins.str]]
    schema_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BudgetAllUpdatesRuleArgs:
    def __init__(
        __self__,
        *,
        disable_default_iam_recipients: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_project_level_recipients: Optional[pulumi.Input[_builtins.bool]] = ...,
        monitoring_notification_channels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableDefaultIamRecipients")
    def disable_default_iam_recipients(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_default_iam_recipients.setter
    def disable_default_iam_recipients(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableProjectLevelRecipients")
    def enable_project_level_recipients(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_project_level_recipients.setter
    def enable_project_level_recipients(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringNotificationChannels")
    def monitoring_notification_channels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @monitoring_notification_channels.setter
    def monitoring_notification_channels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pubsub_topic.setter
    def pubsub_topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_version.setter
    def schema_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BudgetAmountArgsDict(TypedDict):
    last_period_amount: NotRequired[pulumi.Input[_builtins.bool]]
    specified_amount: NotRequired[pulumi.Input[BudgetAmountSpecifiedAmountArgsDict]]
    ...

@pulumi.input_type
class BudgetAmountArgs:
    def __init__(
        __self__,
        *,
        last_period_amount: Optional[pulumi.Input[_builtins.bool]] = ...,
        specified_amount: Optional[pulumi.Input[BudgetAmountSpecifiedAmountArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastPeriodAmount")
    def last_period_amount(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @last_period_amount.setter
    def last_period_amount(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="specifiedAmount")
    def specified_amount(
        self,
    ) -> Optional[pulumi.Input[BudgetAmountSpecifiedAmountArgs]]: ...
    @specified_amount.setter
    def specified_amount(
        self, value: Optional[pulumi.Input[BudgetAmountSpecifiedAmountArgs]]
    ): ...

class BudgetAmountSpecifiedAmountArgsDict(TypedDict):
    currency_code: NotRequired[pulumi.Input[_builtins.str]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    units: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BudgetAmountSpecifiedAmountArgs:
    def __init__(
        __self__,
        *,
        currency_code: Optional[pulumi.Input[_builtins.str]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        units: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @currency_code.setter
    def currency_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def units(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @units.setter
    def units(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BudgetBudgetFilterArgsDict(TypedDict):
    calendar_period: NotRequired[pulumi.Input[_builtins.str]]
    credit_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    credit_types_treatment: NotRequired[pulumi.Input[_builtins.str]]
    custom_period: NotRequired[pulumi.Input[BudgetBudgetFilterCustomPeriodArgsDict]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    projects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_ancestors: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    services: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subaccounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class BudgetBudgetFilterArgs:
    def __init__(
        __self__,
        *,
        calendar_period: Optional[pulumi.Input[_builtins.str]] = ...,
        credit_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        credit_types_treatment: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_period: Optional[pulumi.Input[BudgetBudgetFilterCustomPeriodArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        projects: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        resource_ancestors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        services: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        subaccounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="calendarPeriod")
    def calendar_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @calendar_period.setter
    def calendar_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creditTypes")
    def credit_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @credit_types.setter
    def credit_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creditTypesTreatment")
    def credit_types_treatment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credit_types_treatment.setter
    def credit_types_treatment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customPeriod")
    def custom_period(
        self,
    ) -> Optional[pulumi.Input[BudgetBudgetFilterCustomPeriodArgs]]: ...
    @custom_period.setter
    def custom_period(
        self, value: Optional[pulumi.Input[BudgetBudgetFilterCustomPeriodArgs]]
    ): ...
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
    def projects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @projects.setter
    def projects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAncestors")
    def resource_ancestors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_ancestors.setter
    def resource_ancestors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subaccounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subaccounts.setter
    def subaccounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetBudgetFilterCustomPeriodArgsDict(TypedDict):
    start_date: pulumi.Input[BudgetBudgetFilterCustomPeriodStartDateArgsDict]
    end_date: NotRequired[pulumi.Input[BudgetBudgetFilterCustomPeriodEndDateArgsDict]]
    ...

@pulumi.input_type
class BudgetBudgetFilterCustomPeriodArgs:
    def __init__(
        __self__,
        *,
        start_date: pulumi.Input[BudgetBudgetFilterCustomPeriodStartDateArgs],
        end_date: Optional[
            pulumi.Input[BudgetBudgetFilterCustomPeriodEndDateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(
        self,
    ) -> pulumi.Input[BudgetBudgetFilterCustomPeriodStartDateArgs]: ...
    @start_date.setter
    def start_date(
        self, value: pulumi.Input[BudgetBudgetFilterCustomPeriodStartDateArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(
        self,
    ) -> Optional[pulumi.Input[BudgetBudgetFilterCustomPeriodEndDateArgs]]: ...
    @end_date.setter
    def end_date(
        self, value: Optional[pulumi.Input[BudgetBudgetFilterCustomPeriodEndDateArgs]]
    ): ...

class BudgetBudgetFilterCustomPeriodEndDateArgsDict(TypedDict):
    day: pulumi.Input[_builtins.int]
    month: pulumi.Input[_builtins.int]
    year: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class BudgetBudgetFilterCustomPeriodEndDateArgs:
    def __init__(
        __self__,
        *,
        day: pulumi.Input[_builtins.int],
        month: pulumi.Input[_builtins.int],
        year: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.int]: ...
    @day.setter
    def day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> pulumi.Input[_builtins.int]: ...
    @month.setter
    def month(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> pulumi.Input[_builtins.int]: ...
    @year.setter
    def year(self, value: pulumi.Input[_builtins.int]): ...

class BudgetBudgetFilterCustomPeriodStartDateArgsDict(TypedDict):
    day: pulumi.Input[_builtins.int]
    month: pulumi.Input[_builtins.int]
    year: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class BudgetBudgetFilterCustomPeriodStartDateArgs:
    def __init__(
        __self__,
        *,
        day: pulumi.Input[_builtins.int],
        month: pulumi.Input[_builtins.int],
        year: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.int]: ...
    @day.setter
    def day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> pulumi.Input[_builtins.int]: ...
    @month.setter
    def month(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> pulumi.Input[_builtins.int]: ...
    @year.setter
    def year(self, value: pulumi.Input[_builtins.int]): ...

class BudgetThresholdRuleArgsDict(TypedDict):
    threshold_percent: pulumi.Input[_builtins.float]
    spend_basis: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BudgetThresholdRuleArgs:
    def __init__(
        __self__,
        *,
        threshold_percent: pulumi.Input[_builtins.float],
        spend_basis: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="thresholdPercent")
    def threshold_percent(self) -> pulumi.Input[_builtins.float]: ...
    @threshold_percent.setter
    def threshold_percent(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="spendBasis")
    def spend_basis(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spend_basis.setter
    def spend_basis(self, value: Optional[pulumi.Input[_builtins.str]]): ...

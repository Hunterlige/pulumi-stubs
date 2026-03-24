import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBudgetResult",
    "AwaitableGetBudgetResult",
    "get_budget",
    "get_budget_output",
]

@pulumi.output_type
class GetBudgetResult:
    def __init__(
        __self__,
        account_id=...,
        arn=...,
        auto_adjust_datas=...,
        billing_view_arn=...,
        budget_exceeded=...,
        budget_limits=...,
        budget_type=...,
        calculated_spends=...,
        cost_filters=...,
        cost_types=...,
        id=...,
        name=...,
        name_prefix=...,
        notifications=...,
        planned_limits=...,
        tags=...,
        time_period_end=...,
        time_period_start=...,
        time_unit=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoAdjustDatas")
    def auto_adjust_datas(self) -> Sequence[outputs.GetBudgetAutoAdjustDataResult]: ...
    @_builtins.property
    @pulumi.getter(name="billingViewArn")
    def billing_view_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="budgetExceeded")
    def budget_exceeded(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="budgetLimits")
    def budget_limits(self) -> Sequence[outputs.GetBudgetBudgetLimitResult]: ...
    @_builtins.property
    @pulumi.getter(name="budgetType")
    def budget_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="calculatedSpends")
    def calculated_spends(self) -> Sequence[outputs.GetBudgetCalculatedSpendResult]: ...
    @_builtins.property
    @pulumi.getter(name="costFilters")
    def cost_filters(self) -> Sequence[outputs.GetBudgetCostFilterResult]: ...
    @_builtins.property
    @pulumi.getter(name="costTypes")
    def cost_types(self) -> Sequence[outputs.GetBudgetCostTypeResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Sequence[outputs.GetBudgetNotificationResult]: ...
    @_builtins.property
    @pulumi.getter(name="plannedLimits")
    def planned_limits(self) -> Sequence[outputs.GetBudgetPlannedLimitResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timePeriodEnd")
    def time_period_end(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timePeriodStart")
    def time_period_start(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> _builtins.str: ...

class AwaitableGetBudgetResult(GetBudgetResult):
    def __await__(self): ...

def get_budget(
    account_id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    name_prefix: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBudgetResult: ...
def get_budget_output(
    account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    name_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBudgetResult]: ...

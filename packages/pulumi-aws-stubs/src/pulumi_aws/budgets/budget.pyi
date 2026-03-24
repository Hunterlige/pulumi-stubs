import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BudgetArgs", "Budget"]

@pulumi.input_type
class BudgetArgs:
    def __init__(
        __self__,
        *,
        budget_type: pulumi.Input[_builtins.str],
        time_unit: pulumi.Input[_builtins.str],
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_adjust_data: Optional[pulumi.Input[BudgetAutoAdjustDataArgs]] = ...,
        billing_view_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cost_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetCostFilterArgs]]]
        ] = ...,
        cost_types: Optional[pulumi.Input[BudgetCostTypesArgs]] = ...,
        filter_expression: Optional[pulumi.Input[BudgetFilterExpressionArgs]] = ...,
        limit_amount: Optional[pulumi.Input[_builtins.str]] = ...,
        limit_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetNotificationArgs]]]
        ] = ...,
        planned_limits: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetPlannedLimitArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        time_period_end: Optional[pulumi.Input[_builtins.str]] = ...,
        time_period_start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="budgetType")
    def budget_type(self) -> pulumi.Input[_builtins.str]: ...
    @budget_type.setter
    def budget_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> pulumi.Input[_builtins.str]: ...
    @time_unit.setter
    def time_unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoAdjustData")
    def auto_adjust_data(self) -> Optional[pulumi.Input[BudgetAutoAdjustDataArgs]]: ...
    @auto_adjust_data.setter
    def auto_adjust_data(
        self, value: Optional[pulumi.Input[BudgetAutoAdjustDataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingViewArn")
    def billing_view_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_view_arn.setter
    def billing_view_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="costFilters")
    def cost_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetCostFilterArgs]]]]: ...
    @cost_filters.setter
    def cost_filters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetCostFilterArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="costTypes")
    def cost_types(self) -> Optional[pulumi.Input[BudgetCostTypesArgs]]: ...
    @cost_types.setter
    def cost_types(self, value: Optional[pulumi.Input[BudgetCostTypesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="filterExpression")
    def filter_expression(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionArgs]]: ...
    @filter_expression.setter
    def filter_expression(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitAmount")
    def limit_amount(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @limit_amount.setter
    def limit_amount(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="limitUnit")
    def limit_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @limit_unit.setter
    def limit_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notifications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetNotificationArgs]]]]: ...
    @notifications.setter
    def notifications(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetNotificationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="plannedLimits")
    def planned_limits(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetPlannedLimitArgs]]]]: ...
    @planned_limits.setter
    def planned_limits(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetPlannedLimitArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timePeriodEnd")
    def time_period_end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_period_end.setter
    def time_period_end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timePeriodStart")
    def time_period_start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_period_start.setter
    def time_period_start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BudgetState:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_adjust_data: Optional[pulumi.Input[BudgetAutoAdjustDataArgs]] = ...,
        billing_view_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        budget_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cost_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetCostFilterArgs]]]
        ] = ...,
        cost_types: Optional[pulumi.Input[BudgetCostTypesArgs]] = ...,
        filter_expression: Optional[pulumi.Input[BudgetFilterExpressionArgs]] = ...,
        limit_amount: Optional[pulumi.Input[_builtins.str]] = ...,
        limit_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetNotificationArgs]]]
        ] = ...,
        planned_limits: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetPlannedLimitArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        time_period_end: Optional[pulumi.Input[_builtins.str]] = ...,
        time_period_start: Optional[pulumi.Input[_builtins.str]] = ...,
        time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoAdjustData")
    def auto_adjust_data(self) -> Optional[pulumi.Input[BudgetAutoAdjustDataArgs]]: ...
    @auto_adjust_data.setter
    def auto_adjust_data(
        self, value: Optional[pulumi.Input[BudgetAutoAdjustDataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingViewArn")
    def billing_view_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_view_arn.setter
    def billing_view_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="budgetType")
    def budget_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @budget_type.setter
    def budget_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="costFilters")
    def cost_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetCostFilterArgs]]]]: ...
    @cost_filters.setter
    def cost_filters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetCostFilterArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="costTypes")
    def cost_types(self) -> Optional[pulumi.Input[BudgetCostTypesArgs]]: ...
    @cost_types.setter
    def cost_types(self, value: Optional[pulumi.Input[BudgetCostTypesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="filterExpression")
    def filter_expression(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionArgs]]: ...
    @filter_expression.setter
    def filter_expression(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitAmount")
    def limit_amount(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @limit_amount.setter
    def limit_amount(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="limitUnit")
    def limit_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @limit_unit.setter
    def limit_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notifications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetNotificationArgs]]]]: ...
    @notifications.setter
    def notifications(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetNotificationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="plannedLimits")
    def planned_limits(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetPlannedLimitArgs]]]]: ...
    @planned_limits.setter
    def planned_limits(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetPlannedLimitArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timePeriodEnd")
    def time_period_end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_period_end.setter
    def time_period_end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timePeriodStart")
    def time_period_start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_period_start.setter
    def time_period_start(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_unit.setter
    def time_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:budgets/budget:Budget")
class Budget(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_adjust_data: Optional[
            pulumi.Input[Union[BudgetAutoAdjustDataArgs, BudgetAutoAdjustDataArgsDict]]
        ] = ...,
        billing_view_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        budget_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cost_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[BudgetCostFilterArgs, BudgetCostFilterArgsDict]]
                ]
            ]
        ] = ...,
        cost_types: Optional[
            pulumi.Input[Union[BudgetCostTypesArgs, BudgetCostTypesArgsDict]]
        ] = ...,
        filter_expression: Optional[
            pulumi.Input[
                Union[BudgetFilterExpressionArgs, BudgetFilterExpressionArgsDict]
            ]
        ] = ...,
        limit_amount: Optional[pulumi.Input[_builtins.str]] = ...,
        limit_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BudgetNotificationArgs, BudgetNotificationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        planned_limits: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BudgetPlannedLimitArgs, BudgetPlannedLimitArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        time_period_end: Optional[pulumi.Input[_builtins.str]] = ...,
        time_period_start: Optional[pulumi.Input[_builtins.str]] = ...,
        time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BudgetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_adjust_data: Optional[
            pulumi.Input[Union[BudgetAutoAdjustDataArgs, BudgetAutoAdjustDataArgsDict]]
        ] = ...,
        billing_view_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        budget_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cost_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[BudgetCostFilterArgs, BudgetCostFilterArgsDict]]
                ]
            ]
        ] = ...,
        cost_types: Optional[
            pulumi.Input[Union[BudgetCostTypesArgs, BudgetCostTypesArgsDict]]
        ] = ...,
        filter_expression: Optional[
            pulumi.Input[
                Union[BudgetFilterExpressionArgs, BudgetFilterExpressionArgsDict]
            ]
        ] = ...,
        limit_amount: Optional[pulumi.Input[_builtins.str]] = ...,
        limit_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BudgetNotificationArgs, BudgetNotificationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        planned_limits: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BudgetPlannedLimitArgs, BudgetPlannedLimitArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        time_period_end: Optional[pulumi.Input[_builtins.str]] = ...,
        time_period_start: Optional[pulumi.Input[_builtins.str]] = ...,
        time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Budget: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoAdjustData")
    def auto_adjust_data(
        self,
    ) -> pulumi.Output[Optional[outputs.BudgetAutoAdjustData]]: ...
    @_builtins.property
    @pulumi.getter(name="billingViewArn")
    def billing_view_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="budgetType")
    def budget_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="costFilters")
    def cost_filters(self) -> pulumi.Output[Sequence[outputs.BudgetCostFilter]]: ...
    @_builtins.property
    @pulumi.getter(name="costTypes")
    def cost_types(self) -> pulumi.Output[outputs.BudgetCostTypes]: ...
    @_builtins.property
    @pulumi.getter(name="filterExpression")
    def filter_expression(
        self,
    ) -> pulumi.Output[Optional[outputs.BudgetFilterExpression]]: ...
    @_builtins.property
    @pulumi.getter(name="limitAmount")
    def limit_amount(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="limitUnit")
    def limit_unit(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notifications(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BudgetNotification]]]: ...
    @_builtins.property
    @pulumi.getter(name="plannedLimits")
    def planned_limits(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BudgetPlannedLimit]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timePeriodEnd")
    def time_period_end(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timePeriodStart")
    def time_period_start(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BudgetActionActionThresholdArgs",
    "BudgetActionActionThresholdArgsDict",
    "BudgetActionDefinitionArgs",
    "BudgetActionDefinitionArgsDict",
    "BudgetActionDefinitionIamActionDefinitionArgs",
    "BudgetActionDefinitionIamActionDefinitionArgsDict",
    "BudgetActionDefinitionScpActionDefinitionArgs",
    "BudgetActionDefinitionScpActionDefinitionArgsDict",
    "BudgetActionDefinitionSsmActionDefinitionArgs",
    "BudgetActionDefinitionSsmActionDefinitionArgsDict",
    "BudgetActionSubscriberArgs",
    "BudgetActionSubscriberArgsDict",
    "BudgetAutoAdjustDataArgs",
    "BudgetAutoAdjustDataArgsDict",
    "BudgetAutoAdjustDataHistoricalOptionsArgs",
    "BudgetAutoAdjustDataHistoricalOptionsArgsDict",
    "BudgetCostFilterArgs",
    "BudgetCostFilterArgsDict",
    "BudgetCostTypesArgs",
    "BudgetCostTypesArgsDict",
    "BudgetFilterExpressionArgs",
    "BudgetFilterExpressionArgsDict",
    "BudgetFilterExpressionAndArgs",
    "BudgetFilterExpressionAndArgsDict",
    "BudgetFilterExpressionAndAndArgs",
    "BudgetFilterExpressionAndAndArgsDict",
    "BudgetFilterExpressionAndAndCostCategoriesArgs",
    "BudgetFilterExpressionAndAndCostCategoriesArgsDict",
    "BudgetFilterExpressionAndAndDimensionsArgs",
    "BudgetFilterExpressionAndAndDimensionsArgsDict",
    "BudgetFilterExpressionAndAndTagsArgs",
    "BudgetFilterExpressionAndAndTagsArgsDict",
    "BudgetFilterExpressionAndCostCategoriesArgs",
    "BudgetFilterExpressionAndCostCategoriesArgsDict",
    "BudgetFilterExpressionAndDimensionsArgs",
    "BudgetFilterExpressionAndDimensionsArgsDict",
    "BudgetFilterExpressionAndNotArgs",
    "BudgetFilterExpressionAndNotArgsDict",
    "BudgetFilterExpressionAndNotCostCategoriesArgs",
    "BudgetFilterExpressionAndNotCostCategoriesArgsDict",
    "BudgetFilterExpressionAndNotDimensionsArgs",
    "BudgetFilterExpressionAndNotDimensionsArgsDict",
    "BudgetFilterExpressionAndNotTagsArgs",
    "BudgetFilterExpressionAndNotTagsArgsDict",
    "BudgetFilterExpressionAndOrArgs",
    "BudgetFilterExpressionAndOrArgsDict",
    "BudgetFilterExpressionAndOrCostCategoriesArgs",
    "BudgetFilterExpressionAndOrCostCategoriesArgsDict",
    "BudgetFilterExpressionAndOrDimensionsArgs",
    "BudgetFilterExpressionAndOrDimensionsArgsDict",
    "BudgetFilterExpressionAndOrTagsArgs",
    "BudgetFilterExpressionAndOrTagsArgsDict",
    "BudgetFilterExpressionAndTagsArgs",
    "BudgetFilterExpressionAndTagsArgsDict",
    "BudgetFilterExpressionCostCategoriesArgs",
    "BudgetFilterExpressionCostCategoriesArgsDict",
    "BudgetFilterExpressionDimensionsArgs",
    "BudgetFilterExpressionDimensionsArgsDict",
    "BudgetFilterExpressionNotArgs",
    "BudgetFilterExpressionNotArgsDict",
    "BudgetFilterExpressionNotAndArgs",
    "BudgetFilterExpressionNotAndArgsDict",
    "BudgetFilterExpressionNotAndCostCategoriesArgs",
    "BudgetFilterExpressionNotAndCostCategoriesArgsDict",
    "BudgetFilterExpressionNotAndDimensionsArgs",
    "BudgetFilterExpressionNotAndDimensionsArgsDict",
    "BudgetFilterExpressionNotAndTagsArgs",
    "BudgetFilterExpressionNotAndTagsArgsDict",
    "BudgetFilterExpressionNotCostCategoriesArgs",
    "BudgetFilterExpressionNotCostCategoriesArgsDict",
    "BudgetFilterExpressionNotDimensionsArgs",
    "BudgetFilterExpressionNotDimensionsArgsDict",
    "BudgetFilterExpressionNotNotArgs",
    "BudgetFilterExpressionNotNotArgsDict",
    "BudgetFilterExpressionNotNotCostCategoriesArgs",
    "BudgetFilterExpressionNotNotCostCategoriesArgsDict",
    "BudgetFilterExpressionNotNotDimensionsArgs",
    "BudgetFilterExpressionNotNotDimensionsArgsDict",
    "BudgetFilterExpressionNotNotTagsArgs",
    "BudgetFilterExpressionNotNotTagsArgsDict",
    "BudgetFilterExpressionNotOrArgs",
    "BudgetFilterExpressionNotOrArgsDict",
    "BudgetFilterExpressionNotOrCostCategoriesArgs",
    "BudgetFilterExpressionNotOrCostCategoriesArgsDict",
    "BudgetFilterExpressionNotOrDimensionsArgs",
    "BudgetFilterExpressionNotOrDimensionsArgsDict",
    "BudgetFilterExpressionNotOrTagsArgs",
    "BudgetFilterExpressionNotOrTagsArgsDict",
    "BudgetFilterExpressionNotTagsArgs",
    "BudgetFilterExpressionNotTagsArgsDict",
    "BudgetFilterExpressionOrArgs",
    "BudgetFilterExpressionOrArgsDict",
    "BudgetFilterExpressionOrAndArgs",
    "BudgetFilterExpressionOrAndArgsDict",
    "BudgetFilterExpressionOrAndCostCategoriesArgs",
    "BudgetFilterExpressionOrAndCostCategoriesArgsDict",
    "BudgetFilterExpressionOrAndDimensionsArgs",
    "BudgetFilterExpressionOrAndDimensionsArgsDict",
    "BudgetFilterExpressionOrAndTagsArgs",
    "BudgetFilterExpressionOrAndTagsArgsDict",
    "BudgetFilterExpressionOrCostCategoriesArgs",
    "BudgetFilterExpressionOrCostCategoriesArgsDict",
    "BudgetFilterExpressionOrDimensionsArgs",
    "BudgetFilterExpressionOrDimensionsArgsDict",
    "BudgetFilterExpressionOrNotArgs",
    "BudgetFilterExpressionOrNotArgsDict",
    "BudgetFilterExpressionOrNotCostCategoriesArgs",
    "BudgetFilterExpressionOrNotCostCategoriesArgsDict",
    "BudgetFilterExpressionOrNotDimensionsArgs",
    "BudgetFilterExpressionOrNotDimensionsArgsDict",
    "BudgetFilterExpressionOrNotTagsArgs",
    "BudgetFilterExpressionOrNotTagsArgsDict",
    "BudgetFilterExpressionOrOrArgs",
    "BudgetFilterExpressionOrOrArgsDict",
    "BudgetFilterExpressionOrOrCostCategoriesArgs",
    "BudgetFilterExpressionOrOrCostCategoriesArgsDict",
    "BudgetFilterExpressionOrOrDimensionsArgs",
    "BudgetFilterExpressionOrOrDimensionsArgsDict",
    "BudgetFilterExpressionOrOrTagsArgs",
    "BudgetFilterExpressionOrOrTagsArgsDict",
    "BudgetFilterExpressionOrTagsArgs",
    "BudgetFilterExpressionOrTagsArgsDict",
    "BudgetFilterExpressionTagsArgs",
    "BudgetFilterExpressionTagsArgsDict",
    "BudgetNotificationArgs",
    "BudgetNotificationArgsDict",
    "BudgetPlannedLimitArgs",
    "BudgetPlannedLimitArgsDict",
]

class BudgetActionActionThresholdArgsDict(TypedDict):
    action_threshold_type: pulumi.Input[_builtins.str]
    action_threshold_value: pulumi.Input[_builtins.float]

@pulumi.input_type
class BudgetActionActionThresholdArgs:
    def __init__(
        __self__,
        *,
        action_threshold_type: pulumi.Input[_builtins.str],
        action_threshold_value: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionThresholdType")
    def action_threshold_type(self) -> pulumi.Input[_builtins.str]: ...
    @action_threshold_type.setter
    def action_threshold_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="actionThresholdValue")
    def action_threshold_value(self) -> pulumi.Input[_builtins.float]: ...
    @action_threshold_value.setter
    def action_threshold_value(self, value: pulumi.Input[_builtins.float]): ...

class BudgetActionDefinitionArgsDict(TypedDict):
    iam_action_definition: NotRequired[
        pulumi.Input[BudgetActionDefinitionIamActionDefinitionArgsDict]
    ]
    scp_action_definition: NotRequired[
        pulumi.Input[BudgetActionDefinitionScpActionDefinitionArgsDict]
    ]
    ssm_action_definition: NotRequired[
        pulumi.Input[BudgetActionDefinitionSsmActionDefinitionArgsDict]
    ]

@pulumi.input_type
class BudgetActionDefinitionArgs:
    def __init__(
        __self__,
        *,
        iam_action_definition: Optional[
            pulumi.Input[BudgetActionDefinitionIamActionDefinitionArgs]
        ] = ...,
        scp_action_definition: Optional[
            pulumi.Input[BudgetActionDefinitionScpActionDefinitionArgs]
        ] = ...,
        ssm_action_definition: Optional[
            pulumi.Input[BudgetActionDefinitionSsmActionDefinitionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamActionDefinition")
    def iam_action_definition(
        self,
    ) -> Optional[pulumi.Input[BudgetActionDefinitionIamActionDefinitionArgs]]: ...
    @iam_action_definition.setter
    def iam_action_definition(
        self,
        value: Optional[pulumi.Input[BudgetActionDefinitionIamActionDefinitionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scpActionDefinition")
    def scp_action_definition(
        self,
    ) -> Optional[pulumi.Input[BudgetActionDefinitionScpActionDefinitionArgs]]: ...
    @scp_action_definition.setter
    def scp_action_definition(
        self,
        value: Optional[pulumi.Input[BudgetActionDefinitionScpActionDefinitionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ssmActionDefinition")
    def ssm_action_definition(
        self,
    ) -> Optional[pulumi.Input[BudgetActionDefinitionSsmActionDefinitionArgs]]: ...
    @ssm_action_definition.setter
    def ssm_action_definition(
        self,
        value: Optional[pulumi.Input[BudgetActionDefinitionSsmActionDefinitionArgs]],
    ): ...

class BudgetActionDefinitionIamActionDefinitionArgsDict(TypedDict):
    policy_arn: pulumi.Input[_builtins.str]
    groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    users: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetActionDefinitionIamActionDefinitionArgs:
    def __init__(
        __self__,
        *,
        policy_arn: pulumi.Input[_builtins.str],
        groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        users: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Input[_builtins.str]: ...
    @policy_arn.setter
    def policy_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @groups.setter
    def groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def users(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @users.setter
    def users(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetActionDefinitionScpActionDefinitionArgsDict(TypedDict):
    policy_id: pulumi.Input[_builtins.str]
    target_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BudgetActionDefinitionScpActionDefinitionArgs:
    def __init__(
        __self__,
        *,
        policy_id: pulumi.Input[_builtins.str],
        target_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_id.setter
    def policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetIds")
    def target_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @target_ids.setter
    def target_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class BudgetActionDefinitionSsmActionDefinitionArgsDict(TypedDict):
    action_sub_type: pulumi.Input[_builtins.str]
    instance_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    region: pulumi.Input[_builtins.str]

@pulumi.input_type
class BudgetActionDefinitionSsmActionDefinitionArgs:
    def __init__(
        __self__,
        *,
        action_sub_type: pulumi.Input[_builtins.str],
        instance_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        region: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionSubType")
    def action_sub_type(self) -> pulumi.Input[_builtins.str]: ...
    @action_sub_type.setter
    def action_sub_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @instance_ids.setter
    def instance_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...

class BudgetActionSubscriberArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    subscription_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class BudgetActionSubscriberArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        subscription_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> pulumi.Input[_builtins.str]: ...
    @subscription_type.setter
    def subscription_type(self, value: pulumi.Input[_builtins.str]): ...

class BudgetAutoAdjustDataArgsDict(TypedDict):
    auto_adjust_type: pulumi.Input[_builtins.str]
    historical_options: NotRequired[
        pulumi.Input[BudgetAutoAdjustDataHistoricalOptionsArgsDict]
    ]
    last_auto_adjust_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BudgetAutoAdjustDataArgs:
    def __init__(
        __self__,
        *,
        auto_adjust_type: pulumi.Input[_builtins.str],
        historical_options: Optional[
            pulumi.Input[BudgetAutoAdjustDataHistoricalOptionsArgs]
        ] = ...,
        last_auto_adjust_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoAdjustType")
    def auto_adjust_type(self) -> pulumi.Input[_builtins.str]: ...
    @auto_adjust_type.setter
    def auto_adjust_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="historicalOptions")
    def historical_options(
        self,
    ) -> Optional[pulumi.Input[BudgetAutoAdjustDataHistoricalOptionsArgs]]: ...
    @historical_options.setter
    def historical_options(
        self, value: Optional[pulumi.Input[BudgetAutoAdjustDataHistoricalOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastAutoAdjustTime")
    def last_auto_adjust_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_auto_adjust_time.setter
    def last_auto_adjust_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BudgetAutoAdjustDataHistoricalOptionsArgsDict(TypedDict):
    budget_adjustment_period: pulumi.Input[_builtins.int]
    lookback_available_periods: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BudgetAutoAdjustDataHistoricalOptionsArgs:
    def __init__(
        __self__,
        *,
        budget_adjustment_period: pulumi.Input[_builtins.int],
        lookback_available_periods: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="budgetAdjustmentPeriod")
    def budget_adjustment_period(self) -> pulumi.Input[_builtins.int]: ...
    @budget_adjustment_period.setter
    def budget_adjustment_period(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="lookbackAvailablePeriods")
    def lookback_available_periods(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @lookback_available_periods.setter
    def lookback_available_periods(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class BudgetCostFilterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BudgetCostFilterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class BudgetCostTypesArgsDict(TypedDict):
    include_credit: NotRequired[pulumi.Input[_builtins.bool]]
    include_discount: NotRequired[pulumi.Input[_builtins.bool]]
    include_other_subscription: NotRequired[pulumi.Input[_builtins.bool]]
    include_recurring: NotRequired[pulumi.Input[_builtins.bool]]
    include_refund: NotRequired[pulumi.Input[_builtins.bool]]
    include_subscription: NotRequired[pulumi.Input[_builtins.bool]]
    include_support: NotRequired[pulumi.Input[_builtins.bool]]
    include_tax: NotRequired[pulumi.Input[_builtins.bool]]
    include_upfront: NotRequired[pulumi.Input[_builtins.bool]]
    use_amortized: NotRequired[pulumi.Input[_builtins.bool]]
    use_blended: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BudgetCostTypesArgs:
    def __init__(
        __self__,
        *,
        include_credit: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_discount: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_other_subscription: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_recurring: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_refund: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_subscription: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_tax: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_upfront: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_amortized: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_blended: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeCredit")
    def include_credit(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_credit.setter
    def include_credit(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeDiscount")
    def include_discount(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_discount.setter
    def include_discount(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeOtherSubscription")
    def include_other_subscription(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_other_subscription.setter
    def include_other_subscription(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeRecurring")
    def include_recurring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_recurring.setter
    def include_recurring(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeRefund")
    def include_refund(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_refund.setter
    def include_refund(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeSubscription")
    def include_subscription(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_subscription.setter
    def include_subscription(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeSupport")
    def include_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_support.setter
    def include_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeTax")
    def include_tax(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_tax.setter
    def include_tax(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeUpfront")
    def include_upfront(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_upfront.setter
    def include_upfront(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useAmortized")
    def use_amortized(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_amortized.setter
    def use_amortized(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useBlended")
    def use_blended(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_blended.setter
    def use_blended(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BudgetFilterExpressionArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndArgsDict]]]
    ]
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionDimensionsArgsDict]]
    not_: NotRequired[pulumi.Input[BudgetFilterExpressionNotArgsDict]]
    ors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrArgsDict]]]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndArgs]]]
        ] = ...,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[pulumi.Input[BudgetFilterExpressionDimensionsArgs]] = ...,
        not_: Optional[pulumi.Input[BudgetFilterExpressionNotArgs]] = ...,
        ors: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndArgs]]]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionCostCategoriesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[BudgetFilterExpressionNotArgs]]: ...
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[BudgetFilterExpressionNotArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def ors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrArgs]]]
    ]: ...
    @ors.setter
    def ors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionTagsArgs]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[BudgetFilterExpressionTagsArgs]]): ...

class BudgetFilterExpressionAndArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndAndArgsDict]]]
    ]
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionAndCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionAndDimensionsArgsDict]]
    not_: NotRequired[pulumi.Input[BudgetFilterExpressionAndNotArgsDict]]
    ors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndOrArgsDict]]]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionAndTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionAndArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndAndArgs]]]
        ] = ...,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionAndCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionAndDimensionsArgs]
        ] = ...,
        not_: Optional[pulumi.Input[BudgetFilterExpressionAndNotArgs]] = ...,
        ors: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndOrArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionAndTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndAndArgs]]]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndAndArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndCostCategoriesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[BudgetFilterExpressionAndNotArgs]]: ...
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[BudgetFilterExpressionAndNotArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def ors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndOrArgs]]]
    ]: ...
    @ors.setter
    def ors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionAndOrArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionAndTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndTagsArgs]]
    ): ...

class BudgetFilterExpressionAndAndArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionAndAndCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[
        pulumi.Input[BudgetFilterExpressionAndAndDimensionsArgsDict]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionAndAndTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionAndAndArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionAndAndCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionAndAndDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionAndAndTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndAndCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionAndAndCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndAndDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndAndDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionAndAndTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndAndTagsArgs]]
    ): ...

class BudgetFilterExpressionAndAndCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndAndCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndAndDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndAndDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndAndTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndNotArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionAndNotCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[
        pulumi.Input[BudgetFilterExpressionAndNotDimensionsArgsDict]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionAndNotTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionAndNotArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionAndNotCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionAndNotDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionAndNotTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndNotCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionAndNotCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndNotDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndNotDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionAndNotTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndNotTagsArgs]]
    ): ...

class BudgetFilterExpressionAndNotCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndNotCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndNotDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndNotDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndNotTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndOrArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionAndOrCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionAndOrDimensionsArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionAndOrTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionAndOrArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionAndOrCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionAndOrDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionAndOrTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndOrCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionAndOrCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionAndOrDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndOrDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionAndOrTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionAndOrTagsArgs]]
    ): ...

class BudgetFilterExpressionAndOrCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndOrCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndOrDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndOrDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndOrTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionAndTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotAndArgsDict]]]
    ]
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionNotCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionNotDimensionsArgsDict]]
    not_: NotRequired[pulumi.Input[BudgetFilterExpressionNotNotArgsDict]]
    ors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotOrArgsDict]]]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionNotTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionNotArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotAndArgs]]]
        ] = ...,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionNotCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionNotDimensionsArgs]
        ] = ...,
        not_: Optional[pulumi.Input[BudgetFilterExpressionNotNotArgs]] = ...,
        ors: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotOrArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionNotTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotAndArgs]]]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotAndArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotCostCategoriesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[BudgetFilterExpressionNotNotArgs]]: ...
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[BudgetFilterExpressionNotNotArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def ors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotOrArgs]]]
    ]: ...
    @ors.setter
    def ors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionNotOrArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionNotTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotTagsArgs]]
    ): ...

class BudgetFilterExpressionNotAndArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionNotAndCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[
        pulumi.Input[BudgetFilterExpressionNotAndDimensionsArgsDict]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionNotAndTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionNotAndArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionNotAndCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionNotAndDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionNotAndTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotAndCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionNotAndCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotAndDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotAndDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionNotAndTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotAndTagsArgs]]
    ): ...

class BudgetFilterExpressionNotAndCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotAndCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotAndDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotAndDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotAndTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotNotArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionNotNotCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[
        pulumi.Input[BudgetFilterExpressionNotNotDimensionsArgsDict]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionNotNotTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionNotNotArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionNotNotCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionNotNotDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionNotNotTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotNotCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionNotNotCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotNotDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotNotDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionNotNotTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotNotTagsArgs]]
    ): ...

class BudgetFilterExpressionNotNotCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotNotCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotNotDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotNotDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotNotTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotOrArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionNotOrCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionNotOrDimensionsArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionNotOrTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionNotOrArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionNotOrCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionNotOrDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionNotOrTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotOrCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionNotOrCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionNotOrDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotOrDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionNotOrTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionNotOrTagsArgs]]
    ): ...

class BudgetFilterExpressionNotOrCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotOrCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotOrDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotOrDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotOrTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionNotTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrAndArgsDict]]]
    ]
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionOrCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionOrDimensionsArgsDict]]
    not_: NotRequired[pulumi.Input[BudgetFilterExpressionOrNotArgsDict]]
    ors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrOrArgsDict]]]
    ]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionOrTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionOrArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrAndArgs]]]
        ] = ...,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionOrCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionOrDimensionsArgs]
        ] = ...,
        not_: Optional[pulumi.Input[BudgetFilterExpressionOrNotArgs]] = ...,
        ors: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrOrArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionOrTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrAndArgs]]]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrAndArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrCostCategoriesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[BudgetFilterExpressionOrNotArgs]]: ...
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[BudgetFilterExpressionOrNotArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def ors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrOrArgs]]]
    ]: ...
    @ors.setter
    def ors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterExpressionOrOrArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionOrTagsArgs]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[BudgetFilterExpressionOrTagsArgs]]): ...

class BudgetFilterExpressionOrAndArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionOrAndCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionOrAndDimensionsArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionOrAndTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionOrAndArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionOrAndCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionOrAndDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionOrAndTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrAndCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionOrAndCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrAndDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrAndDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionOrAndTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrAndTagsArgs]]
    ): ...

class BudgetFilterExpressionOrAndCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrAndCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrAndDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrAndDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrAndTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrNotArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionOrNotCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionOrNotDimensionsArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionOrNotTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionOrNotArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionOrNotCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionOrNotDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionOrNotTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrNotCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionOrNotCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrNotDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrNotDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionOrNotTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrNotTagsArgs]]
    ): ...

class BudgetFilterExpressionOrNotCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrNotCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrNotDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrNotDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrNotTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrOrArgsDict(TypedDict):
    cost_categories: NotRequired[
        pulumi.Input[BudgetFilterExpressionOrOrCostCategoriesArgsDict]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetFilterExpressionOrOrDimensionsArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetFilterExpressionOrOrTagsArgsDict]]

@pulumi.input_type
class BudgetFilterExpressionOrOrArgs:
    def __init__(
        __self__,
        *,
        cost_categories: Optional[
            pulumi.Input[BudgetFilterExpressionOrOrCostCategoriesArgs]
        ] = ...,
        dimensions: Optional[
            pulumi.Input[BudgetFilterExpressionOrOrDimensionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[BudgetFilterExpressionOrOrTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrOrCostCategoriesArgs]]: ...
    @cost_categories.setter
    def cost_categories(
        self,
        value: Optional[pulumi.Input[BudgetFilterExpressionOrOrCostCategoriesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[BudgetFilterExpressionOrOrDimensionsArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrOrDimensionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetFilterExpressionOrOrTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[BudgetFilterExpressionOrOrTagsArgs]]
    ): ...

class BudgetFilterExpressionOrOrCostCategoriesArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrOrCostCategoriesArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrOrDimensionsArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrOrDimensionsArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrOrTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionOrTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetFilterExpressionTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BudgetFilterExpressionTagsArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        match_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @match_options.setter
    def match_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetNotificationArgsDict(TypedDict):
    comparison_operator: pulumi.Input[_builtins.str]
    notification_type: pulumi.Input[_builtins.str]
    threshold: pulumi.Input[_builtins.float]
    threshold_type: pulumi.Input[_builtins.str]
    subscriber_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    subscriber_sns_topic_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class BudgetNotificationArgs:
    def __init__(
        __self__,
        *,
        comparison_operator: pulumi.Input[_builtins.str],
        notification_type: pulumi.Input[_builtins.str],
        threshold: pulumi.Input[_builtins.float],
        threshold_type: pulumi.Input[_builtins.str],
        subscriber_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subscriber_sns_topic_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> pulumi.Input[_builtins.str]: ...
    @comparison_operator.setter
    def comparison_operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Input[_builtins.str]: ...
    @notification_type.setter
    def notification_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.float]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="thresholdType")
    def threshold_type(self) -> pulumi.Input[_builtins.str]: ...
    @threshold_type.setter
    def threshold_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subscriberEmailAddresses")
    def subscriber_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subscriber_email_addresses.setter
    def subscriber_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriberSnsTopicArns")
    def subscriber_sns_topic_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subscriber_sns_topic_arns.setter
    def subscriber_sns_topic_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BudgetPlannedLimitArgsDict(TypedDict):
    amount: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[_builtins.str]
    unit: pulumi.Input[_builtins.str]

@pulumi.input_type
class BudgetPlannedLimitArgs:
    def __init__(
        __self__,
        *,
        amount: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[_builtins.str],
        unit: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> pulumi.Input[_builtins.str]: ...
    @amount.setter
    def amount(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...



import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BudgetActionActionThreshold', 'BudgetActionDefinition', 'BudgetActionDefinitionIamActionDefinition', 'BudgetActionDefinitionScpActionDefinition', 'BudgetActionDefinitionSsmActionDefinition', 'BudgetActionSubscriber', 'BudgetAutoAdjustData', 'BudgetAutoAdjustDataHistoricalOptions', 'BudgetCostFilter', 'BudgetCostTypes', 'BudgetFilterExpression', 'BudgetFilterExpressionAnd', 'BudgetFilterExpressionAndAnd', 'BudgetFilterExpressionAndAndCostCategories', 'BudgetFilterExpressionAndAndDimensions', 'BudgetFilterExpressionAndAndTags', 'BudgetFilterExpressionAndCostCategories', 'BudgetFilterExpressionAndDimensions', 'BudgetFilterExpressionAndNot', 'BudgetFilterExpressionAndNotCostCategories', 'BudgetFilterExpressionAndNotDimensions', 'BudgetFilterExpressionAndNotTags', 'BudgetFilterExpressionAndOr', 'BudgetFilterExpressionAndOrCostCategories', 'BudgetFilterExpressionAndOrDimensions', 'BudgetFilterExpressionAndOrTags', 'BudgetFilterExpressionAndTags', 'BudgetFilterExpressionCostCategories', 'BudgetFilterExpressionDimensions', 'BudgetFilterExpressionNot', 'BudgetFilterExpressionNotAnd', 'BudgetFilterExpressionNotAndCostCategories', 'BudgetFilterExpressionNotAndDimensions', 'BudgetFilterExpressionNotAndTags', 'BudgetFilterExpressionNotCostCategories', 'BudgetFilterExpressionNotDimensions', 'BudgetFilterExpressionNotNot', 'BudgetFilterExpressionNotNotCostCategories', 'BudgetFilterExpressionNotNotDimensions', 'BudgetFilterExpressionNotNotTags', 'BudgetFilterExpressionNotOr', 'BudgetFilterExpressionNotOrCostCategories', 'BudgetFilterExpressionNotOrDimensions', 'BudgetFilterExpressionNotOrTags', 'BudgetFilterExpressionNotTags', 'BudgetFilterExpressionOr', 'BudgetFilterExpressionOrAnd', 'BudgetFilterExpressionOrAndCostCategories', 'BudgetFilterExpressionOrAndDimensions', 'BudgetFilterExpressionOrAndTags', 'BudgetFilterExpressionOrCostCategories', 'BudgetFilterExpressionOrDimensions', 'BudgetFilterExpressionOrNot', 'BudgetFilterExpressionOrNotCostCategories', 'BudgetFilterExpressionOrNotDimensions', 'BudgetFilterExpressionOrNotTags', 'BudgetFilterExpressionOrOr', 'BudgetFilterExpressionOrOrCostCategories', 'BudgetFilterExpressionOrOrDimensions', 'BudgetFilterExpressionOrOrTags', 'BudgetFilterExpressionOrTags', 'BudgetFilterExpressionTags', 'BudgetNotification', 'BudgetPlannedLimit', 'GetBudgetAutoAdjustDataResult', 'GetBudgetAutoAdjustDataHistoricalOptionResult', 'GetBudgetBudgetLimitResult', 'GetBudgetCalculatedSpendResult', 'GetBudgetCalculatedSpendActualSpendResult', 'GetBudgetCostFilterResult', 'GetBudgetCostTypeResult', 'GetBudgetNotificationResult', 'GetBudgetPlannedLimitResult']
@pulumi.output_type
class BudgetActionActionThreshold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_threshold_type: _builtins.str, action_threshold_value: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionThresholdType")
    def action_threshold_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionThresholdValue")
    def action_threshold_value(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class BudgetActionDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, iam_action_definition: Optional[outputs.BudgetActionDefinitionIamActionDefinition] = ..., scp_action_definition: Optional[outputs.BudgetActionDefinitionScpActionDefinition] = ..., ssm_action_definition: Optional[outputs.BudgetActionDefinitionSsmActionDefinition] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamActionDefinition")
    def iam_action_definition(self) -> Optional[outputs.BudgetActionDefinitionIamActionDefinition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scpActionDefinition")
    def scp_action_definition(self) -> Optional[outputs.BudgetActionDefinitionScpActionDefinition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmActionDefinition")
    def ssm_action_definition(self) -> Optional[outputs.BudgetActionDefinitionSsmActionDefinition]:
        
        ...
    


@pulumi.output_type
class BudgetActionDefinitionIamActionDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_arn: _builtins.str, groups: Optional[Sequence[_builtins.str]] = ..., roles: Optional[Sequence[_builtins.str]] = ..., users: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetActionDefinitionScpActionDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_id: _builtins.str, target_ids: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIds")
    def target_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BudgetActionDefinitionSsmActionDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_sub_type: _builtins.str, instance_ids: Sequence[_builtins.str], region: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionSubType")
    def action_sub_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BudgetActionSubscriber(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: _builtins.str, subscription_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BudgetAutoAdjustData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_adjust_type: _builtins.str, historical_options: Optional[outputs.BudgetAutoAdjustDataHistoricalOptions] = ..., last_auto_adjust_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoAdjustType")
    def auto_adjust_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="historicalOptions")
    def historical_options(self) -> Optional[outputs.BudgetAutoAdjustDataHistoricalOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAutoAdjustTime")
    def last_auto_adjust_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BudgetAutoAdjustDataHistoricalOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, budget_adjustment_period: _builtins.int, lookback_available_periods: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetAdjustmentPeriod")
    def budget_adjustment_period(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackAvailablePeriods")
    def lookback_available_periods(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BudgetCostFilter(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BudgetCostTypes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_credit: Optional[_builtins.bool] = ..., include_discount: Optional[_builtins.bool] = ..., include_other_subscription: Optional[_builtins.bool] = ..., include_recurring: Optional[_builtins.bool] = ..., include_refund: Optional[_builtins.bool] = ..., include_subscription: Optional[_builtins.bool] = ..., include_support: Optional[_builtins.bool] = ..., include_tax: Optional[_builtins.bool] = ..., include_upfront: Optional[_builtins.bool] = ..., use_amortized: Optional[_builtins.bool] = ..., use_blended: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCredit")
    def include_credit(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeDiscount")
    def include_discount(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeOtherSubscription")
    def include_other_subscription(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRecurring")
    def include_recurring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRefund")
    def include_refund(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSubscription")
    def include_subscription(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSupport")
    def include_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTax")
    def include_tax(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeUpfront")
    def include_upfront(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useAmortized")
    def use_amortized(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useBlended")
    def use_blended(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ands: Optional[Sequence[outputs.BudgetFilterExpressionAnd]] = ..., cost_categories: Optional[outputs.BudgetFilterExpressionCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionDimensions] = ..., not_: Optional[outputs.BudgetFilterExpressionNot] = ..., ors: Optional[Sequence[outputs.BudgetFilterExpressionOr]] = ..., tags: Optional[outputs.BudgetFilterExpressionTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.BudgetFilterExpressionAnd]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.BudgetFilterExpressionNot]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.BudgetFilterExpressionOr]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAnd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ands: Optional[Sequence[outputs.BudgetFilterExpressionAndAnd]] = ..., cost_categories: Optional[outputs.BudgetFilterExpressionAndCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionAndDimensions] = ..., not_: Optional[outputs.BudgetFilterExpressionAndNot] = ..., ors: Optional[Sequence[outputs.BudgetFilterExpressionAndOr]] = ..., tags: Optional[outputs.BudgetFilterExpressionAndTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.BudgetFilterExpressionAndAnd]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionAndCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionAndDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.BudgetFilterExpressionAndNot]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.BudgetFilterExpressionAndOr]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionAndTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndAnd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionAndAndCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionAndAndDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionAndAndTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionAndAndCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionAndAndDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionAndAndTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndAndCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndAndDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndAndTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndNot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionAndNotCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionAndNotDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionAndNotTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionAndNotCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionAndNotDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionAndNotTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndNotCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndNotDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndNotTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndOr(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionAndOrCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionAndOrDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionAndOrTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionAndOrCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionAndOrDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionAndOrTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndOrCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndOrDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndOrTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionAndTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ands: Optional[Sequence[outputs.BudgetFilterExpressionNotAnd]] = ..., cost_categories: Optional[outputs.BudgetFilterExpressionNotCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionNotDimensions] = ..., not_: Optional[outputs.BudgetFilterExpressionNotNot] = ..., ors: Optional[Sequence[outputs.BudgetFilterExpressionNotOr]] = ..., tags: Optional[outputs.BudgetFilterExpressionNotTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.BudgetFilterExpressionNotAnd]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionNotCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionNotDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.BudgetFilterExpressionNotNot]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.BudgetFilterExpressionNotOr]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionNotTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotAnd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionNotAndCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionNotAndDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionNotAndTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionNotAndCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionNotAndDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionNotAndTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotAndCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotAndDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotAndTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotNot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionNotNotCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionNotNotDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionNotNotTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionNotNotCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionNotNotDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionNotNotTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotNotCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotNotDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotNotTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotOr(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionNotOrCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionNotOrDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionNotOrTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionNotOrCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionNotOrDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionNotOrTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotOrCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotOrDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotOrTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionNotTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOr(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ands: Optional[Sequence[outputs.BudgetFilterExpressionOrAnd]] = ..., cost_categories: Optional[outputs.BudgetFilterExpressionOrCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionOrDimensions] = ..., not_: Optional[outputs.BudgetFilterExpressionOrNot] = ..., ors: Optional[Sequence[outputs.BudgetFilterExpressionOrOr]] = ..., tags: Optional[outputs.BudgetFilterExpressionOrTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.BudgetFilterExpressionOrAnd]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionOrCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionOrDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.BudgetFilterExpressionOrNot]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.BudgetFilterExpressionOrOr]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionOrTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrAnd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionOrAndCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionOrAndDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionOrAndTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionOrAndCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionOrAndDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionOrAndTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrAndCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrAndDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrAndTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrNot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionOrNotCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionOrNotDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionOrNotTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionOrNotCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionOrNotDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionOrNotTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrNotCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrNotDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrNotTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrOr(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cost_categories: Optional[outputs.BudgetFilterExpressionOrOrCostCategories] = ..., dimensions: Optional[outputs.BudgetFilterExpressionOrOrDimensions] = ..., tags: Optional[outputs.BudgetFilterExpressionOrOrTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(self) -> Optional[outputs.BudgetFilterExpressionOrOrCostCategories]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetFilterExpressionOrOrDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetFilterExpressionOrOrTags]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrOrCostCategories(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrOrDimensions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], match_options: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrOrTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionOrTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetFilterExpressionTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetNotification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison_operator: _builtins.str, notification_type: _builtins.str, threshold: _builtins.float, threshold_type: _builtins.str, subscriber_email_addresses: Optional[Sequence[_builtins.str]] = ..., subscriber_sns_topic_arns: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdType")
    def threshold_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberEmailAddresses")
    def subscriber_email_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberSnsTopicArns")
    def subscriber_sns_topic_arns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BudgetPlannedLimit(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amount: _builtins.str, start_time: _builtins.str, unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBudgetAutoAdjustDataResult(dict):
    def __init__(__self__, *, auto_adjust_type: _builtins.str, historical_options: Sequence[outputs.GetBudgetAutoAdjustDataHistoricalOptionResult], last_auto_adjust_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoAdjustType")
    def auto_adjust_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="historicalOptions")
    def historical_options(self) -> Sequence[outputs.GetBudgetAutoAdjustDataHistoricalOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAutoAdjustTime")
    def last_auto_adjust_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBudgetAutoAdjustDataHistoricalOptionResult(dict):
    def __init__(__self__, *, budget_adjustment_period: _builtins.int, lookback_available_periods: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetAdjustmentPeriod")
    def budget_adjustment_period(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackAvailablePeriods")
    def lookback_available_periods(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetBudgetBudgetLimitResult(dict):
    def __init__(__self__, *, amount: _builtins.str, unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBudgetCalculatedSpendResult(dict):
    def __init__(__self__, *, actual_spends: Sequence[outputs.GetBudgetCalculatedSpendActualSpendResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actualSpends")
    def actual_spends(self) -> Sequence[outputs.GetBudgetCalculatedSpendActualSpendResult]:
        ...
    


@pulumi.output_type
class GetBudgetCalculatedSpendActualSpendResult(dict):
    def __init__(__self__, *, amount: _builtins.str, unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBudgetCostFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetBudgetCostTypeResult(dict):
    def __init__(__self__, *, include_credit: _builtins.bool, include_discount: _builtins.bool, include_other_subscription: _builtins.bool, include_recurring: _builtins.bool, include_refund: _builtins.bool, include_subscription: _builtins.bool, include_support: _builtins.bool, include_tax: _builtins.bool, include_upfront: _builtins.bool, use_amortized: _builtins.bool, use_blended: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCredit")
    def include_credit(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeDiscount")
    def include_discount(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeOtherSubscription")
    def include_other_subscription(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRecurring")
    def include_recurring(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRefund")
    def include_refund(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSubscription")
    def include_subscription(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSupport")
    def include_support(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTax")
    def include_tax(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeUpfront")
    def include_upfront(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useAmortized")
    def use_amortized(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useBlended")
    def use_blended(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetBudgetNotificationResult(dict):
    def __init__(__self__, *, comparison_operator: _builtins.str, notification_type: _builtins.str, subscriber_email_addresses: Sequence[_builtins.str], subscriber_sns_topic_arns: Sequence[_builtins.str], threshold: _builtins.float, threshold_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberEmailAddresses")
    def subscriber_email_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberSnsTopicArns")
    def subscriber_sns_topic_arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdType")
    def threshold_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBudgetPlannedLimitResult(dict):
    def __init__(__self__, *, amount: _builtins.str, start_time: _builtins.str, unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    



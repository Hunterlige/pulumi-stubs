

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnomalySubscriptionSubscriberArgs', 'AnomalySubscriptionSubscriberArgsDict', 'AnomalySubscriptionThresholdExpressionArgs', 'AnomalySubscriptionThresholdExpressionArgsDict', 'AnomalySubscriptionThresholdExpressionAndArgs', 'AnomalySubscriptionThresholdExpressionAndArgsDict', ..., ..., ..., ..., 'AnomalySubscriptionThresholdExpressionAndTagsArgs', ..., ..., ..., ..., ..., 'AnomalySubscriptionThresholdExpressionNotArgs', 'AnomalySubscriptionThresholdExpressionNotArgsDict', ..., ..., ..., ..., 'AnomalySubscriptionThresholdExpressionNotTagsArgs', ..., 'AnomalySubscriptionThresholdExpressionOrArgs', 'AnomalySubscriptionThresholdExpressionOrArgsDict', ..., ..., ..., ..., 'AnomalySubscriptionThresholdExpressionOrTagsArgs', ..., 'AnomalySubscriptionThresholdExpressionTagsArgs', 'AnomalySubscriptionThresholdExpressionTagsArgsDict', 'CostCategoryRuleArgs', 'CostCategoryRuleArgsDict', 'CostCategoryRuleInheritedValueArgs', 'CostCategoryRuleInheritedValueArgsDict', 'CostCategoryRuleRuleArgs', 'CostCategoryRuleRuleArgsDict', 'CostCategoryRuleRuleAndArgs', 'CostCategoryRuleRuleAndArgsDict', 'CostCategoryRuleRuleAndAndArgs', 'CostCategoryRuleRuleAndAndArgsDict', 'CostCategoryRuleRuleAndAndCostCategoryArgs', 'CostCategoryRuleRuleAndAndCostCategoryArgsDict', 'CostCategoryRuleRuleAndAndDimensionArgs', 'CostCategoryRuleRuleAndAndDimensionArgsDict', 'CostCategoryRuleRuleAndAndTagsArgs', 'CostCategoryRuleRuleAndAndTagsArgsDict', 'CostCategoryRuleRuleAndCostCategoryArgs', 'CostCategoryRuleRuleAndCostCategoryArgsDict', 'CostCategoryRuleRuleAndDimensionArgs', 'CostCategoryRuleRuleAndDimensionArgsDict', 'CostCategoryRuleRuleAndNotArgs', 'CostCategoryRuleRuleAndNotArgsDict', 'CostCategoryRuleRuleAndNotCostCategoryArgs', 'CostCategoryRuleRuleAndNotCostCategoryArgsDict', 'CostCategoryRuleRuleAndNotDimensionArgs', 'CostCategoryRuleRuleAndNotDimensionArgsDict', 'CostCategoryRuleRuleAndNotTagsArgs', 'CostCategoryRuleRuleAndNotTagsArgsDict', 'CostCategoryRuleRuleAndOrArgs', 'CostCategoryRuleRuleAndOrArgsDict', 'CostCategoryRuleRuleAndOrCostCategoryArgs', 'CostCategoryRuleRuleAndOrCostCategoryArgsDict', 'CostCategoryRuleRuleAndOrDimensionArgs', 'CostCategoryRuleRuleAndOrDimensionArgsDict', 'CostCategoryRuleRuleAndOrTagsArgs', 'CostCategoryRuleRuleAndOrTagsArgsDict', 'CostCategoryRuleRuleAndTagsArgs', 'CostCategoryRuleRuleAndTagsArgsDict', 'CostCategoryRuleRuleCostCategoryArgs', 'CostCategoryRuleRuleCostCategoryArgsDict', 'CostCategoryRuleRuleDimensionArgs', 'CostCategoryRuleRuleDimensionArgsDict', 'CostCategoryRuleRuleNotArgs', 'CostCategoryRuleRuleNotArgsDict', 'CostCategoryRuleRuleNotAndArgs', 'CostCategoryRuleRuleNotAndArgsDict', 'CostCategoryRuleRuleNotAndCostCategoryArgs', 'CostCategoryRuleRuleNotAndCostCategoryArgsDict', 'CostCategoryRuleRuleNotAndDimensionArgs', 'CostCategoryRuleRuleNotAndDimensionArgsDict', 'CostCategoryRuleRuleNotAndTagsArgs', 'CostCategoryRuleRuleNotAndTagsArgsDict', 'CostCategoryRuleRuleNotCostCategoryArgs', 'CostCategoryRuleRuleNotCostCategoryArgsDict', 'CostCategoryRuleRuleNotDimensionArgs', 'CostCategoryRuleRuleNotDimensionArgsDict', 'CostCategoryRuleRuleNotNotArgs', 'CostCategoryRuleRuleNotNotArgsDict', 'CostCategoryRuleRuleNotNotCostCategoryArgs', 'CostCategoryRuleRuleNotNotCostCategoryArgsDict', 'CostCategoryRuleRuleNotNotDimensionArgs', 'CostCategoryRuleRuleNotNotDimensionArgsDict', 'CostCategoryRuleRuleNotNotTagsArgs', 'CostCategoryRuleRuleNotNotTagsArgsDict', 'CostCategoryRuleRuleNotOrArgs', 'CostCategoryRuleRuleNotOrArgsDict', 'CostCategoryRuleRuleNotOrCostCategoryArgs', 'CostCategoryRuleRuleNotOrCostCategoryArgsDict', 'CostCategoryRuleRuleNotOrDimensionArgs', 'CostCategoryRuleRuleNotOrDimensionArgsDict', 'CostCategoryRuleRuleNotOrTagsArgs', 'CostCategoryRuleRuleNotOrTagsArgsDict', 'CostCategoryRuleRuleNotTagsArgs', 'CostCategoryRuleRuleNotTagsArgsDict', 'CostCategoryRuleRuleOrArgs', 'CostCategoryRuleRuleOrArgsDict', 'CostCategoryRuleRuleOrAndArgs', 'CostCategoryRuleRuleOrAndArgsDict', 'CostCategoryRuleRuleOrAndCostCategoryArgs', 'CostCategoryRuleRuleOrAndCostCategoryArgsDict', 'CostCategoryRuleRuleOrAndDimensionArgs', 'CostCategoryRuleRuleOrAndDimensionArgsDict', 'CostCategoryRuleRuleOrAndTagsArgs', 'CostCategoryRuleRuleOrAndTagsArgsDict', 'CostCategoryRuleRuleOrCostCategoryArgs', 'CostCategoryRuleRuleOrCostCategoryArgsDict', 'CostCategoryRuleRuleOrDimensionArgs', 'CostCategoryRuleRuleOrDimensionArgsDict', 'CostCategoryRuleRuleOrNotArgs', 'CostCategoryRuleRuleOrNotArgsDict', 'CostCategoryRuleRuleOrNotCostCategoryArgs', 'CostCategoryRuleRuleOrNotCostCategoryArgsDict', 'CostCategoryRuleRuleOrNotDimensionArgs', 'CostCategoryRuleRuleOrNotDimensionArgsDict', 'CostCategoryRuleRuleOrNotTagsArgs', 'CostCategoryRuleRuleOrNotTagsArgsDict', 'CostCategoryRuleRuleOrOrArgs', 'CostCategoryRuleRuleOrOrArgsDict', 'CostCategoryRuleRuleOrOrCostCategoryArgs', 'CostCategoryRuleRuleOrOrCostCategoryArgsDict', 'CostCategoryRuleRuleOrOrDimensionArgs', 'CostCategoryRuleRuleOrOrDimensionArgsDict', 'CostCategoryRuleRuleOrOrTagsArgs', 'CostCategoryRuleRuleOrOrTagsArgsDict', 'CostCategoryRuleRuleOrTagsArgs', 'CostCategoryRuleRuleOrTagsArgsDict', 'CostCategoryRuleRuleTagsArgs', 'CostCategoryRuleRuleTagsArgsDict', 'CostCategorySplitChargeRuleArgs', 'CostCategorySplitChargeRuleArgsDict', 'CostCategorySplitChargeRuleParameterArgs', 'CostCategorySplitChargeRuleParameterArgsDict', 'GetTagsFilterArgs', 'GetTagsFilterArgsDict', 'GetTagsFilterAndArgs', 'GetTagsFilterAndArgsDict', 'GetTagsFilterAndCostCategoryArgs', 'GetTagsFilterAndCostCategoryArgsDict', 'GetTagsFilterAndDimensionArgs', 'GetTagsFilterAndDimensionArgsDict', 'GetTagsFilterAndTagsArgs', 'GetTagsFilterAndTagsArgsDict', 'GetTagsFilterCostCategoryArgs', 'GetTagsFilterCostCategoryArgsDict', 'GetTagsFilterDimensionArgs', 'GetTagsFilterDimensionArgsDict', 'GetTagsFilterNotArgs', 'GetTagsFilterNotArgsDict', 'GetTagsFilterNotCostCategoryArgs', 'GetTagsFilterNotCostCategoryArgsDict', 'GetTagsFilterNotDimensionArgs', 'GetTagsFilterNotDimensionArgsDict', 'GetTagsFilterNotTagsArgs', 'GetTagsFilterNotTagsArgsDict', 'GetTagsFilterOrArgs', 'GetTagsFilterOrArgsDict', 'GetTagsFilterOrCostCategoryArgs', 'GetTagsFilterOrCostCategoryArgsDict', 'GetTagsFilterOrDimensionArgs', 'GetTagsFilterOrDimensionArgsDict', 'GetTagsFilterOrTagsArgs', 'GetTagsFilterOrTagsArgsDict', 'GetTagsFilterTagsArgs', 'GetTagsFilterTagsArgsDict', 'GetTagsSortByArgs', 'GetTagsSortByArgsDict', 'GetTagsTimePeriodArgs', 'GetTagsTimePeriodArgsDict']
class AnomalySubscriptionSubscriberArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnomalySubscriptionSubscriberArgs:
    def __init__(__self__, *, address: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionArgsDict(TypedDict):
    ands: NotRequired[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionAndArgsDict]]]]
    cost_category: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionDimensionArgsDict]]
    not_: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionNotArgsDict]]
    ors: NotRequired[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionOrArgsDict]]]]
    tags: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionTagsArgsDict]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionArgs:
    def __init__(__self__, *, ands: Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionAndArgs]]]] = ..., cost_category: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionDimensionArgs]] = ..., not_: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotArgs]] = ..., ors: Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionOrArgs]]]] = ..., tags: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionAndArgs]]]]:
        
        ...
    
    @ands.setter
    def ands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionAndArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotArgs]]:
        
        ...
    
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionOrArgs]]]]:
        
        ...
    
    @ors.setter
    def ors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionThresholdExpressionOrArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionTagsArgs]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionAndArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionAndCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionAndDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionAndTagsArgsDict]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionAndArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndDimensionArgs]] = ..., tags: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionAndTagsArgs]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionAndCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionAndCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionAndDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionAndDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionAndTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionNotArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionNotCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionNotDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionNotTagsArgsDict]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionNotArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotDimensionArgs]] = ..., tags: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionNotTagsArgs]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionNotCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionNotCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionNotDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionNotDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionNotTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionOrArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionOrCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionOrDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[AnomalySubscriptionThresholdExpressionOrTagsArgsDict]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionOrArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrDimensionArgs]] = ..., tags: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionOrTagsArgs]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionOrCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionOrCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionOrDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionOrDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionOrTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnomalySubscriptionThresholdExpressionTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnomalySubscriptionThresholdExpressionTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleArgsDict(TypedDict):
    inherited_value: NotRequired[pulumi.Input[CostCategoryRuleInheritedValueArgsDict]]
    rule: NotRequired[pulumi.Input[CostCategoryRuleRuleArgsDict]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CostCategoryRuleArgs:
    def __init__(__self__, *, inherited_value: Optional[pulumi.Input[CostCategoryRuleInheritedValueArgs]] = ..., rule: Optional[pulumi.Input[CostCategoryRuleRuleArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritedValue")
    def inherited_value(self) -> Optional[pulumi.Input[CostCategoryRuleInheritedValueArgs]]:
        
        ...
    
    @inherited_value.setter
    def inherited_value(self, value: Optional[pulumi.Input[CostCategoryRuleInheritedValueArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input[CostCategoryRuleRuleArgs]]:
        
        ...
    
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[CostCategoryRuleRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CostCategoryRuleInheritedValueArgsDict(TypedDict):
    dimension_key: NotRequired[pulumi.Input[_builtins.str]]
    dimension_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CostCategoryRuleInheritedValueArgs:
    def __init__(__self__, *, dimension_key: Optional[pulumi.Input[_builtins.str]] = ..., dimension_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dimensionKey")
    def dimension_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dimension_key.setter
    def dimension_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dimension_name.setter
    def dimension_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CostCategoryRuleRuleArgsDict(TypedDict):
    ands: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndArgsDict]]]]
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleDimensionArgsDict]]
    not_: NotRequired[pulumi.Input[CostCategoryRuleRuleNotArgsDict]]
    ors: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrArgsDict]]]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleArgs:
    def __init__(__self__, *, ands: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndArgs]]]] = ..., cost_category: Optional[pulumi.Input[CostCategoryRuleRuleCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleDimensionArgs]] = ..., not_: Optional[pulumi.Input[CostCategoryRuleRuleNotArgs]] = ..., ors: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrArgs]]]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndArgs]]]]:
        
        ...
    
    @ands.setter
    def ands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotArgs]]:
        
        ...
    
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrArgs]]]]:
        
        ...
    
    @ors.setter
    def ors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndArgsDict(TypedDict):
    ands: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndAndArgsDict]]]]
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleAndCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleAndDimensionArgsDict]]
    not_: NotRequired[pulumi.Input[CostCategoryRuleRuleAndNotArgsDict]]
    ors: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndOrArgsDict]]]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleAndTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleAndArgs:
    def __init__(__self__, *, ands: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndAndArgs]]]] = ..., cost_category: Optional[pulumi.Input[CostCategoryRuleRuleAndCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleAndDimensionArgs]] = ..., not_: Optional[pulumi.Input[CostCategoryRuleRuleAndNotArgs]] = ..., ors: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndOrArgs]]]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleAndTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndAndArgs]]]]:
        
        ...
    
    @ands.setter
    def ands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndAndArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndNotArgs]]:
        
        ...
    
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndNotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndOrArgs]]]]:
        
        ...
    
    @ors.setter
    def ors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleAndOrArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndAndArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleAndAndCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleAndAndDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleAndAndTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleAndAndArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleAndAndCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleAndAndDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleAndAndTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndAndCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndAndCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndAndDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndAndDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndAndTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndAndTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndAndCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndAndCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndAndDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndAndDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndAndTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndNotArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleAndNotCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleAndNotDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleAndNotTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleAndNotArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleAndNotCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleAndNotDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleAndNotTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndNotCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndNotCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndNotDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndNotDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndNotTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndNotTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndNotCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndNotCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndNotDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndNotDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndNotTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndOrArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleAndOrCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleAndOrDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleAndOrTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleAndOrArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleAndOrCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleAndOrDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleAndOrTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndOrCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndOrCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndOrDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndOrDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleAndOrTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleAndOrTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndOrCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndOrCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndOrDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndOrDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndOrTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleAndTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotArgsDict(TypedDict):
    ands: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotAndArgsDict]]]]
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleNotCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleNotDimensionArgsDict]]
    not_: NotRequired[pulumi.Input[CostCategoryRuleRuleNotNotArgsDict]]
    ors: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotOrArgsDict]]]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleNotTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleNotArgs:
    def __init__(__self__, *, ands: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotAndArgs]]]] = ..., cost_category: Optional[pulumi.Input[CostCategoryRuleRuleNotCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleNotDimensionArgs]] = ..., not_: Optional[pulumi.Input[CostCategoryRuleRuleNotNotArgs]] = ..., ors: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotOrArgs]]]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleNotTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotAndArgs]]]]:
        
        ...
    
    @ands.setter
    def ands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotAndArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotNotArgs]]:
        
        ...
    
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotNotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotOrArgs]]]]:
        
        ...
    
    @ors.setter
    def ors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleNotOrArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotAndArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleNotAndCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleNotAndDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleNotAndTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleNotAndArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleNotAndCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleNotAndDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleNotAndTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotAndCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotAndCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotAndDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotAndDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotAndTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotAndTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotAndCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotAndCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotAndDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotAndDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotAndTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotNotArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleNotNotCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleNotNotDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleNotNotTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleNotNotArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleNotNotCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleNotNotDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleNotNotTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotNotCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotNotCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotNotDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotNotDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotNotTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotNotTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotNotCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotNotCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotNotDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotNotDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotNotTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotOrArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleNotOrCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleNotOrDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleNotOrTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleNotOrArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleNotOrCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleNotOrDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleNotOrTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotOrCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotOrCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotOrDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotOrDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleNotOrTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleNotOrTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotOrCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotOrCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotOrDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotOrDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotOrTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleNotTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrArgsDict(TypedDict):
    ands: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrAndArgsDict]]]]
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleOrCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleOrDimensionArgsDict]]
    not_: NotRequired[pulumi.Input[CostCategoryRuleRuleOrNotArgsDict]]
    ors: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrOrArgsDict]]]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleOrTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleOrArgs:
    def __init__(__self__, *, ands: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrAndArgs]]]] = ..., cost_category: Optional[pulumi.Input[CostCategoryRuleRuleOrCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleOrDimensionArgs]] = ..., not_: Optional[pulumi.Input[CostCategoryRuleRuleOrNotArgs]] = ..., ors: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrOrArgs]]]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleOrTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrAndArgs]]]]:
        
        ...
    
    @ands.setter
    def ands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrAndArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrNotArgs]]:
        
        ...
    
    @not_.setter
    def not_(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrNotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrOrArgs]]]]:
        
        ...
    
    @ors.setter
    def ors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategoryRuleRuleOrOrArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrAndArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleOrAndCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleOrAndDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleOrAndTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleOrAndArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleOrAndCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleOrAndDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleOrAndTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrAndCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrAndCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrAndDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrAndDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrAndTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrAndTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrAndCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrAndCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrAndDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrAndDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrAndTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrAndTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrNotArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleOrNotCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleOrNotDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleOrNotTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleOrNotArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleOrNotCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleOrNotDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleOrNotTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrNotCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrNotCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrNotDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrNotDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrNotTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrNotTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrNotCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrNotCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrNotDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrNotDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrNotTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrNotTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrOrArgsDict(TypedDict):
    cost_category: NotRequired[pulumi.Input[CostCategoryRuleRuleOrOrCostCategoryArgsDict]]
    dimension: NotRequired[pulumi.Input[CostCategoryRuleRuleOrOrDimensionArgsDict]]
    tags: NotRequired[pulumi.Input[CostCategoryRuleRuleOrOrTagsArgsDict]]


@pulumi.input_type
class CostCategoryRuleRuleOrOrArgs:
    def __init__(__self__, *, cost_category: Optional[pulumi.Input[CostCategoryRuleRuleOrOrCostCategoryArgs]] = ..., dimension: Optional[pulumi.Input[CostCategoryRuleRuleOrOrDimensionArgs]] = ..., tags: Optional[pulumi.Input[CostCategoryRuleRuleOrOrTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrOrCostCategoryArgs]]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrOrCostCategoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrOrDimensionArgs]]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrOrDimensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[CostCategoryRuleRuleOrOrTagsArgs]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[CostCategoryRuleRuleOrOrTagsArgs]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrOrCostCategoryArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrOrCostCategoryArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrOrDimensionArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrOrDimensionArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrOrTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleOrTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleOrTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategoryRuleRuleTagsArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    match_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategoryRuleRuleTagsArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., match_options: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CostCategorySplitChargeRuleArgsDict(TypedDict):
    method: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]
    targets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleParameterArgsDict]]]]


@pulumi.input_type
class CostCategorySplitChargeRuleArgs:
    def __init__(__self__, *, method: pulumi.Input[_builtins.str], source: pulumi.Input[_builtins.str], targets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @method.setter
    def method(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CostCategorySplitChargeRuleParameterArgs]]]]): # -> None:
        ...
    


class CostCategorySplitChargeRuleParameterArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CostCategorySplitChargeRuleParameterArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class GetTagsFilterArgsDict(TypedDict):
    ands: NotRequired[Sequence[GetTagsFilterAndArgsDict]]
    cost_category: NotRequired[GetTagsFilterCostCategoryArgsDict]
    dimension: NotRequired[GetTagsFilterDimensionArgsDict]
    not_: NotRequired[GetTagsFilterNotArgsDict]
    ors: NotRequired[Sequence[GetTagsFilterOrArgsDict]]
    tags: NotRequired[GetTagsFilterTagsArgsDict]


@pulumi.input_type
class GetTagsFilterArgs:
    def __init__(__self__, *, ands: Optional[Sequence[GetTagsFilterAndArgs]] = ..., cost_category: Optional[GetTagsFilterCostCategoryArgs] = ..., dimension: Optional[GetTagsFilterDimensionArgs] = ..., not_: Optional[GetTagsFilterNotArgs] = ..., ors: Optional[Sequence[GetTagsFilterOrArgs]] = ..., tags: Optional[GetTagsFilterTagsArgs] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[GetTagsFilterAndArgs]]:
        
        ...
    
    @ands.setter
    def ands(self, value: Optional[Sequence[GetTagsFilterAndArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[GetTagsFilterCostCategoryArgs]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[GetTagsFilterCostCategoryArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[GetTagsFilterDimensionArgs]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[GetTagsFilterDimensionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[GetTagsFilterNotArgs]:
        
        ...
    
    @not_.setter
    def not_(self, value: Optional[GetTagsFilterNotArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[GetTagsFilterOrArgs]]:
        
        ...
    
    @ors.setter
    def ors(self, value: Optional[Sequence[GetTagsFilterOrArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[GetTagsFilterTagsArgs]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[GetTagsFilterTagsArgs]): # -> None:
        ...
    


class GetTagsFilterAndArgsDict(TypedDict):
    cost_category: NotRequired[GetTagsFilterAndCostCategoryArgsDict]
    dimension: NotRequired[GetTagsFilterAndDimensionArgsDict]
    tags: NotRequired[GetTagsFilterAndTagsArgsDict]


@pulumi.input_type
class GetTagsFilterAndArgs:
    def __init__(__self__, *, cost_category: Optional[GetTagsFilterAndCostCategoryArgs] = ..., dimension: Optional[GetTagsFilterAndDimensionArgs] = ..., tags: Optional[GetTagsFilterAndTagsArgs] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[GetTagsFilterAndCostCategoryArgs]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[GetTagsFilterAndCostCategoryArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[GetTagsFilterAndDimensionArgs]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[GetTagsFilterAndDimensionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[GetTagsFilterAndTagsArgs]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[GetTagsFilterAndTagsArgs]): # -> None:
        ...
    


class GetTagsFilterAndCostCategoryArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterAndCostCategoryArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterAndDimensionArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterAndDimensionArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterAndTagsArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterAndTagsArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterCostCategoryArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterCostCategoryArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterDimensionArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterDimensionArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterNotArgsDict(TypedDict):
    cost_category: NotRequired[GetTagsFilterNotCostCategoryArgsDict]
    dimension: NotRequired[GetTagsFilterNotDimensionArgsDict]
    tags: NotRequired[GetTagsFilterNotTagsArgsDict]


@pulumi.input_type
class GetTagsFilterNotArgs:
    def __init__(__self__, *, cost_category: Optional[GetTagsFilterNotCostCategoryArgs] = ..., dimension: Optional[GetTagsFilterNotDimensionArgs] = ..., tags: Optional[GetTagsFilterNotTagsArgs] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[GetTagsFilterNotCostCategoryArgs]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[GetTagsFilterNotCostCategoryArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[GetTagsFilterNotDimensionArgs]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[GetTagsFilterNotDimensionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[GetTagsFilterNotTagsArgs]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[GetTagsFilterNotTagsArgs]): # -> None:
        ...
    


class GetTagsFilterNotCostCategoryArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterNotCostCategoryArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterNotDimensionArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterNotDimensionArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterNotTagsArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterNotTagsArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterOrArgsDict(TypedDict):
    cost_category: NotRequired[GetTagsFilterOrCostCategoryArgsDict]
    dimension: NotRequired[GetTagsFilterOrDimensionArgsDict]
    tags: NotRequired[GetTagsFilterOrTagsArgsDict]


@pulumi.input_type
class GetTagsFilterOrArgs:
    def __init__(__self__, *, cost_category: Optional[GetTagsFilterOrCostCategoryArgs] = ..., dimension: Optional[GetTagsFilterOrDimensionArgs] = ..., tags: Optional[GetTagsFilterOrTagsArgs] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[GetTagsFilterOrCostCategoryArgs]:
        
        ...
    
    @cost_category.setter
    def cost_category(self, value: Optional[GetTagsFilterOrCostCategoryArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[GetTagsFilterOrDimensionArgs]:
        
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[GetTagsFilterOrDimensionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[GetTagsFilterOrTagsArgs]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[GetTagsFilterOrTagsArgs]): # -> None:
        ...
    


class GetTagsFilterOrCostCategoryArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterOrCostCategoryArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterOrDimensionArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterOrDimensionArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterOrTagsArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterOrTagsArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsFilterTagsArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    match_options: NotRequired[Sequence[_builtins.str]]
    values: NotRequired[Sequence[_builtins.str]]


@pulumi.input_type
class GetTagsFilterTagsArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., match_options: Optional[Sequence[_builtins.str]] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @match_options.setter
    def match_options(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[_builtins.str]]): # -> None:
        ...
    


class GetTagsSortByArgsDict(TypedDict):
    key: NotRequired[_builtins.str]
    sort_order: NotRequired[_builtins.str]


@pulumi.input_type
class GetTagsSortByArgs:
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., sort_order: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[_builtins.str]:
        
        ...
    
    @sort_order.setter
    def sort_order(self, value: Optional[_builtins.str]): # -> None:
        ...
    


class GetTagsTimePeriodArgsDict(TypedDict):
    end: _builtins.str
    start: _builtins.str


@pulumi.input_type
class GetTagsTimePeriodArgs:
    def __init__(__self__, *, end: _builtins.str, start: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.str:
        
        ...
    
    @end.setter
    def end(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.str:
        
        ...
    
    @start.setter
    def start(self, value: _builtins.str): # -> None:
        ...
    



import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AnomalySubscriptionSubscriber",
    "AnomalySubscriptionThresholdExpression",
    "AnomalySubscriptionThresholdExpressionAnd",
    ...,
    "AnomalySubscriptionThresholdExpressionAndDimension",
    "AnomalySubscriptionThresholdExpressionAndTags",
    "AnomalySubscriptionThresholdExpressionCostCategory",
    "AnomalySubscriptionThresholdExpressionDimension",
    "AnomalySubscriptionThresholdExpressionNot",
    ...,
    "AnomalySubscriptionThresholdExpressionNotDimension",
    "AnomalySubscriptionThresholdExpressionNotTags",
    "AnomalySubscriptionThresholdExpressionOr",
    ...,
    "AnomalySubscriptionThresholdExpressionOrDimension",
    "AnomalySubscriptionThresholdExpressionOrTags",
    "AnomalySubscriptionThresholdExpressionTags",
    "CostCategoryRule",
    "CostCategoryRuleInheritedValue",
    "CostCategoryRuleRule",
    "CostCategoryRuleRuleAnd",
    "CostCategoryRuleRuleAndAnd",
    "CostCategoryRuleRuleAndAndCostCategory",
    "CostCategoryRuleRuleAndAndDimension",
    "CostCategoryRuleRuleAndAndTags",
    "CostCategoryRuleRuleAndCostCategory",
    "CostCategoryRuleRuleAndDimension",
    "CostCategoryRuleRuleAndNot",
    "CostCategoryRuleRuleAndNotCostCategory",
    "CostCategoryRuleRuleAndNotDimension",
    "CostCategoryRuleRuleAndNotTags",
    "CostCategoryRuleRuleAndOr",
    "CostCategoryRuleRuleAndOrCostCategory",
    "CostCategoryRuleRuleAndOrDimension",
    "CostCategoryRuleRuleAndOrTags",
    "CostCategoryRuleRuleAndTags",
    "CostCategoryRuleRuleCostCategory",
    "CostCategoryRuleRuleDimension",
    "CostCategoryRuleRuleNot",
    "CostCategoryRuleRuleNotAnd",
    "CostCategoryRuleRuleNotAndCostCategory",
    "CostCategoryRuleRuleNotAndDimension",
    "CostCategoryRuleRuleNotAndTags",
    "CostCategoryRuleRuleNotCostCategory",
    "CostCategoryRuleRuleNotDimension",
    "CostCategoryRuleRuleNotNot",
    "CostCategoryRuleRuleNotNotCostCategory",
    "CostCategoryRuleRuleNotNotDimension",
    "CostCategoryRuleRuleNotNotTags",
    "CostCategoryRuleRuleNotOr",
    "CostCategoryRuleRuleNotOrCostCategory",
    "CostCategoryRuleRuleNotOrDimension",
    "CostCategoryRuleRuleNotOrTags",
    "CostCategoryRuleRuleNotTags",
    "CostCategoryRuleRuleOr",
    "CostCategoryRuleRuleOrAnd",
    "CostCategoryRuleRuleOrAndCostCategory",
    "CostCategoryRuleRuleOrAndDimension",
    "CostCategoryRuleRuleOrAndTags",
    "CostCategoryRuleRuleOrCostCategory",
    "CostCategoryRuleRuleOrDimension",
    "CostCategoryRuleRuleOrNot",
    "CostCategoryRuleRuleOrNotCostCategory",
    "CostCategoryRuleRuleOrNotDimension",
    "CostCategoryRuleRuleOrNotTags",
    "CostCategoryRuleRuleOrOr",
    "CostCategoryRuleRuleOrOrCostCategory",
    "CostCategoryRuleRuleOrOrDimension",
    "CostCategoryRuleRuleOrOrTags",
    "CostCategoryRuleRuleOrTags",
    "CostCategoryRuleRuleTags",
    "CostCategorySplitChargeRule",
    "CostCategorySplitChargeRuleParameter",
    "GetCostCategoryRuleResult",
    "GetCostCategoryRuleInheritedValueResult",
    "GetCostCategoryRuleRuleResult",
    "GetCostCategoryRuleRuleAndResult",
    "GetCostCategoryRuleRuleAndAndResult",
    "GetCostCategoryRuleRuleAndAndCostCategoryResult",
    "GetCostCategoryRuleRuleAndAndDimensionResult",
    "GetCostCategoryRuleRuleAndAndTagResult",
    "GetCostCategoryRuleRuleAndCostCategoryResult",
    "GetCostCategoryRuleRuleAndDimensionResult",
    "GetCostCategoryRuleRuleAndNotResult",
    "GetCostCategoryRuleRuleAndNotCostCategoryResult",
    "GetCostCategoryRuleRuleAndNotDimensionResult",
    "GetCostCategoryRuleRuleAndNotTagResult",
    "GetCostCategoryRuleRuleAndOrResult",
    "GetCostCategoryRuleRuleAndOrCostCategoryResult",
    "GetCostCategoryRuleRuleAndOrDimensionResult",
    "GetCostCategoryRuleRuleAndOrTagResult",
    "GetCostCategoryRuleRuleAndTagResult",
    "GetCostCategoryRuleRuleCostCategoryResult",
    "GetCostCategoryRuleRuleDimensionResult",
    "GetCostCategoryRuleRuleNotResult",
    "GetCostCategoryRuleRuleNotAndResult",
    "GetCostCategoryRuleRuleNotAndCostCategoryResult",
    "GetCostCategoryRuleRuleNotAndDimensionResult",
    "GetCostCategoryRuleRuleNotAndTagResult",
    "GetCostCategoryRuleRuleNotCostCategoryResult",
    "GetCostCategoryRuleRuleNotDimensionResult",
    "GetCostCategoryRuleRuleNotNotResult",
    "GetCostCategoryRuleRuleNotNotCostCategoryResult",
    "GetCostCategoryRuleRuleNotNotDimensionResult",
    "GetCostCategoryRuleRuleNotNotTagResult",
    "GetCostCategoryRuleRuleNotOrResult",
    "GetCostCategoryRuleRuleNotOrCostCategoryResult",
    "GetCostCategoryRuleRuleNotOrDimensionResult",
    "GetCostCategoryRuleRuleNotOrTagResult",
    "GetCostCategoryRuleRuleNotTagResult",
    "GetCostCategoryRuleRuleOrResult",
    "GetCostCategoryRuleRuleOrAndResult",
    "GetCostCategoryRuleRuleOrAndCostCategoryResult",
    "GetCostCategoryRuleRuleOrAndDimensionResult",
    "GetCostCategoryRuleRuleOrAndTagResult",
    "GetCostCategoryRuleRuleOrCostCategoryResult",
    "GetCostCategoryRuleRuleOrDimensionResult",
    "GetCostCategoryRuleRuleOrNotResult",
    "GetCostCategoryRuleRuleOrNotCostCategoryResult",
    "GetCostCategoryRuleRuleOrNotDimensionResult",
    "GetCostCategoryRuleRuleOrNotTagResult",
    "GetCostCategoryRuleRuleOrOrResult",
    "GetCostCategoryRuleRuleOrOrCostCategoryResult",
    "GetCostCategoryRuleRuleOrOrDimensionResult",
    "GetCostCategoryRuleRuleOrOrTagResult",
    "GetCostCategoryRuleRuleOrTagResult",
    "GetCostCategoryRuleRuleTagResult",
    "GetCostCategorySplitChargeRuleResult",
    "GetCostCategorySplitChargeRuleParameterResult",
    "GetTagsFilterResult",
    "GetTagsFilterAndResult",
    "GetTagsFilterAndCostCategoryResult",
    "GetTagsFilterAndDimensionResult",
    "GetTagsFilterAndTagsResult",
    "GetTagsFilterCostCategoryResult",
    "GetTagsFilterDimensionResult",
    "GetTagsFilterNotResult",
    "GetTagsFilterNotCostCategoryResult",
    "GetTagsFilterNotDimensionResult",
    "GetTagsFilterNotTagsResult",
    "GetTagsFilterOrResult",
    "GetTagsFilterOrCostCategoryResult",
    "GetTagsFilterOrDimensionResult",
    "GetTagsFilterOrTagsResult",
    "GetTagsFilterTagsResult",
    "GetTagsSortByResult",
    "GetTagsTimePeriodResult",
]

@pulumi.output_type
class AnomalySubscriptionSubscriber(dict):
    def __init__(__self__, *, address: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpression(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ands: Optional[
            Sequence[outputs.AnomalySubscriptionThresholdExpressionAnd]
        ] = ...,
        cost_category: Optional[
            outputs.AnomalySubscriptionThresholdExpressionCostCategory
        ] = ...,
        dimension: Optional[
            outputs.AnomalySubscriptionThresholdExpressionDimension
        ] = ...,
        not_: Optional[outputs.AnomalySubscriptionThresholdExpressionNot] = ...,
        ors: Optional[Sequence[outputs.AnomalySubscriptionThresholdExpressionOr]] = ...,
        tags: Optional[outputs.AnomalySubscriptionThresholdExpressionTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[Sequence[outputs.AnomalySubscriptionThresholdExpressionAnd]]: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionDimension]: ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.AnomalySubscriptionThresholdExpressionNot]: ...
    @_builtins.property
    @pulumi.getter
    def ors(
        self,
    ) -> Optional[Sequence[outputs.AnomalySubscriptionThresholdExpressionOr]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.AnomalySubscriptionThresholdExpressionTags]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[
            outputs.AnomalySubscriptionThresholdExpressionAndCostCategory
        ] = ...,
        dimension: Optional[
            outputs.AnomalySubscriptionThresholdExpressionAndDimension
        ] = ...,
        tags: Optional[outputs.AnomalySubscriptionThresholdExpressionAndTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionAndCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionAndDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionAndTags]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionAndCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionAndDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionAndTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionNot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[
            outputs.AnomalySubscriptionThresholdExpressionNotCostCategory
        ] = ...,
        dimension: Optional[
            outputs.AnomalySubscriptionThresholdExpressionNotDimension
        ] = ...,
        tags: Optional[outputs.AnomalySubscriptionThresholdExpressionNotTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionNotCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionNotDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionNotTags]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionNotCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionNotDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionNotTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionOr(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[
            outputs.AnomalySubscriptionThresholdExpressionOrCostCategory
        ] = ...,
        dimension: Optional[
            outputs.AnomalySubscriptionThresholdExpressionOrDimension
        ] = ...,
        tags: Optional[outputs.AnomalySubscriptionThresholdExpressionOrTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionOrCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionOrDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[outputs.AnomalySubscriptionThresholdExpressionOrTags]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionOrCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionOrDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionOrTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnomalySubscriptionThresholdExpressionTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inherited_value: Optional[outputs.CostCategoryRuleInheritedValue] = ...,
        rule: Optional[outputs.CostCategoryRuleRule] = ...,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inheritedValue")
    def inherited_value(self) -> Optional[outputs.CostCategoryRuleInheritedValue]: ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> Optional[outputs.CostCategoryRuleRule]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CostCategoryRuleInheritedValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimension_key: Optional[_builtins.str] = ...,
        dimension_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dimensionKey")
    def dimension_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CostCategoryRuleRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ands: Optional[Sequence[outputs.CostCategoryRuleRuleAnd]] = ...,
        cost_category: Optional[outputs.CostCategoryRuleRuleCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleDimension] = ...,
        not_: Optional[outputs.CostCategoryRuleRuleNot] = ...,
        ors: Optional[Sequence[outputs.CostCategoryRuleRuleOr]] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleAnd]]: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[outputs.CostCategoryRuleRuleCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleDimension]: ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.CostCategoryRuleRuleNot]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleOr]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ands: Optional[Sequence[outputs.CostCategoryRuleRuleAndAnd]] = ...,
        cost_category: Optional[outputs.CostCategoryRuleRuleAndCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleAndDimension] = ...,
        not_: Optional[outputs.CostCategoryRuleRuleAndNot] = ...,
        ors: Optional[Sequence[outputs.CostCategoryRuleRuleAndOr]] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleAndTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleAndAnd]]: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleAndCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleAndDimension]: ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.CostCategoryRuleRuleAndNot]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleAndOr]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleAndTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleAndAndCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleAndAndDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleAndAndTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleAndAndCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleAndAndDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleAndAndTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndAndCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndAndDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndAndTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndNot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleAndNotCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleAndNotDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleAndNotTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleAndNotCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleAndNotDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleAndNotTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndNotCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndNotDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndNotTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndOr(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleAndOrCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleAndOrDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleAndOrTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleAndOrCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleAndOrDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleAndOrTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndOrCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndOrDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndOrTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleAndTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ands: Optional[Sequence[outputs.CostCategoryRuleRuleNotAnd]] = ...,
        cost_category: Optional[outputs.CostCategoryRuleRuleNotCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleNotDimension] = ...,
        not_: Optional[outputs.CostCategoryRuleRuleNotNot] = ...,
        ors: Optional[Sequence[outputs.CostCategoryRuleRuleNotOr]] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleNotTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleNotAnd]]: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleNotCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleNotDimension]: ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.CostCategoryRuleRuleNotNot]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleNotOr]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleNotTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleNotAndCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleNotAndDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleNotAndTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleNotAndCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleNotAndDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleNotAndTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotAndCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotAndDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotAndTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotNot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleNotNotCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleNotNotDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleNotNotTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleNotNotCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleNotNotDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleNotNotTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotNotCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotNotDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotNotTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotOr(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleNotOrCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleNotOrDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleNotOrTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleNotOrCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleNotOrDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleNotOrTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotOrCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotOrDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotOrTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleNotTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOr(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ands: Optional[Sequence[outputs.CostCategoryRuleRuleOrAnd]] = ...,
        cost_category: Optional[outputs.CostCategoryRuleRuleOrCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleOrDimension] = ...,
        not_: Optional[outputs.CostCategoryRuleRuleOrNot] = ...,
        ors: Optional[Sequence[outputs.CostCategoryRuleRuleOrOr]] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleOrTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleOrAnd]]: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[outputs.CostCategoryRuleRuleOrCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleOrDimension]: ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.CostCategoryRuleRuleOrNot]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.CostCategoryRuleRuleOrOr]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleOrTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleOrAndCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleOrAndDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleOrAndTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleOrAndCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleOrAndDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleOrAndTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrAndCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrAndDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrAndTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrNot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleOrNotCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleOrNotDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleOrNotTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleOrNotCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleOrNotDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleOrNotTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrNotCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrNotDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrNotTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrOr(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.CostCategoryRuleRuleOrOrCostCategory] = ...,
        dimension: Optional[outputs.CostCategoryRuleRuleOrOrDimension] = ...,
        tags: Optional[outputs.CostCategoryRuleRuleOrOrTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(
        self,
    ) -> Optional[outputs.CostCategoryRuleRuleOrOrCostCategory]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.CostCategoryRuleRuleOrOrDimension]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.CostCategoryRuleRuleOrOrTags]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrOrCostCategory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrOrDimension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrOrTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleOrTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategoryRuleRuleTags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CostCategorySplitChargeRule(dict):
    def __init__(
        __self__,
        *,
        method: _builtins.str,
        source: _builtins.str,
        targets: Sequence[_builtins.str],
        parameters: Optional[
            Sequence[outputs.CostCategorySplitChargeRuleParameter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.CostCategorySplitChargeRuleParameter]]: ...

@pulumi.output_type
class CostCategorySplitChargeRuleParameter(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetCostCategoryRuleResult(dict):
    def __init__(
        __self__,
        *,
        inherited_values: Sequence[outputs.GetCostCategoryRuleInheritedValueResult],
        rules: Sequence[outputs.GetCostCategoryRuleRuleResult],
        type: _builtins.str,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inheritedValues")
    def inherited_values(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleInheritedValueResult]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetCostCategoryRuleRuleResult]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetCostCategoryRuleInheritedValueResult(dict):
    def __init__(
        __self__, *, dimension_key: _builtins.str, dimension_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dimensionKey")
    def dimension_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetCostCategoryRuleRuleResult(dict):
    def __init__(
        __self__,
        *,
        ands: Sequence[outputs.GetCostCategoryRuleRuleAndResult],
        cost_categories: Sequence[outputs.GetCostCategoryRuleRuleCostCategoryResult],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleDimensionResult],
        nots: Sequence[outputs.GetCostCategoryRuleRuleNotResult],
        ors: Sequence[outputs.GetCostCategoryRuleRuleOrResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndResult]: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def nots(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotResult]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndResult(dict):
    def __init__(
        __self__,
        *,
        ands: Sequence[outputs.GetCostCategoryRuleRuleAndAndResult],
        cost_categories: Sequence[outputs.GetCostCategoryRuleRuleAndCostCategoryResult],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleAndDimensionResult],
        nots: Sequence[outputs.GetCostCategoryRuleRuleAndNotResult],
        ors: Sequence[outputs.GetCostCategoryRuleRuleAndOrResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleAndTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndAndResult]: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def nots(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndNotResult]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndOrResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndAndResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleAndAndCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleAndAndDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleAndAndTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndAndCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndAndDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndAndTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndAndCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndAndDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndAndTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndNotResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleAndNotCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleAndNotDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleAndNotTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndNotCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndNotDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndNotTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndNotCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndNotDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndNotTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndOrResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleAndOrCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleAndOrDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleAndOrTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndOrCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleAndOrDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleAndOrTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndOrCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndOrDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndOrTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleAndTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotResult(dict):
    def __init__(
        __self__,
        *,
        ands: Sequence[outputs.GetCostCategoryRuleRuleNotAndResult],
        cost_categories: Sequence[outputs.GetCostCategoryRuleRuleNotCostCategoryResult],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleNotDimensionResult],
        nots: Sequence[outputs.GetCostCategoryRuleRuleNotNotResult],
        ors: Sequence[outputs.GetCostCategoryRuleRuleNotOrResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleNotTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotAndResult]: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def nots(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotNotResult]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotOrResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotAndResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleNotAndCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleNotAndDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleNotAndTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotAndCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotAndDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotAndTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotAndCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotAndDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotAndTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotNotResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleNotNotCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleNotNotDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleNotNotTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotNotCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotNotDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotNotTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotNotCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotNotDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotNotTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotOrResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleNotOrCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleNotOrDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleNotOrTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotOrCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleNotOrDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleNotOrTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotOrCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotOrDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotOrTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleNotTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrResult(dict):
    def __init__(
        __self__,
        *,
        ands: Sequence[outputs.GetCostCategoryRuleRuleOrAndResult],
        cost_categories: Sequence[outputs.GetCostCategoryRuleRuleOrCostCategoryResult],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleOrDimensionResult],
        nots: Sequence[outputs.GetCostCategoryRuleRuleOrNotResult],
        ors: Sequence[outputs.GetCostCategoryRuleRuleOrOrResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleOrTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrAndResult]: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def nots(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrNotResult]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrOrResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrAndResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleOrAndCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleOrAndDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleOrAndTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrAndCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrAndDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrAndTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrAndCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrAndDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrAndTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrNotResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleOrNotCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleOrNotDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleOrNotTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrNotCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrNotDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrNotTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrNotCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrNotDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrNotTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrOrResult(dict):
    def __init__(
        __self__,
        *,
        cost_categories: Sequence[
            outputs.GetCostCategoryRuleRuleOrOrCostCategoryResult
        ],
        dimensions: Sequence[outputs.GetCostCategoryRuleRuleOrOrDimensionResult],
        tags: Sequence[outputs.GetCostCategoryRuleRuleOrOrTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategories")
    def cost_categories(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrOrCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Sequence[outputs.GetCostCategoryRuleRuleOrOrDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[outputs.GetCostCategoryRuleRuleOrOrTagResult]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrOrCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrOrDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrOrTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleOrTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategoryRuleRuleTagResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        match_options: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategorySplitChargeRuleResult(dict):
    def __init__(
        __self__,
        *,
        method: _builtins.str,
        parameters: Sequence[outputs.GetCostCategorySplitChargeRuleParameterResult],
        source: _builtins.str,
        targets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Sequence[outputs.GetCostCategorySplitChargeRuleParameterResult]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCostCategorySplitChargeRuleParameterResult(dict):
    def __init__(
        __self__, *, type: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetTagsFilterResult(dict):
    def __init__(
        __self__,
        *,
        ands: Optional[Sequence[outputs.GetTagsFilterAndResult]] = ...,
        cost_category: Optional[outputs.GetTagsFilterCostCategoryResult] = ...,
        dimension: Optional[outputs.GetTagsFilterDimensionResult] = ...,
        not_: Optional[outputs.GetTagsFilterNotResult] = ...,
        ors: Optional[Sequence[outputs.GetTagsFilterOrResult]] = ...,
        tags: Optional[outputs.GetTagsFilterTagsResult] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(self) -> Optional[Sequence[outputs.GetTagsFilterAndResult]]: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[outputs.GetTagsFilterCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.GetTagsFilterDimensionResult]: ...
    @_builtins.property
    @pulumi.getter(name="not")
    def not_(self) -> Optional[outputs.GetTagsFilterNotResult]: ...
    @_builtins.property
    @pulumi.getter
    def ors(self) -> Optional[Sequence[outputs.GetTagsFilterOrResult]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.GetTagsFilterTagsResult]: ...

@pulumi.output_type
class GetTagsFilterAndResult(dict):
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.GetTagsFilterAndCostCategoryResult] = ...,
        dimension: Optional[outputs.GetTagsFilterAndDimensionResult] = ...,
        tags: Optional[outputs.GetTagsFilterAndTagsResult] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[outputs.GetTagsFilterAndCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.GetTagsFilterAndDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.GetTagsFilterAndTagsResult]: ...

@pulumi.output_type
class GetTagsFilterAndCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterAndDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterAndTagsResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterNotResult(dict):
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.GetTagsFilterNotCostCategoryResult] = ...,
        dimension: Optional[outputs.GetTagsFilterNotDimensionResult] = ...,
        tags: Optional[outputs.GetTagsFilterNotTagsResult] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[outputs.GetTagsFilterNotCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.GetTagsFilterNotDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.GetTagsFilterNotTagsResult]: ...

@pulumi.output_type
class GetTagsFilterNotCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterNotDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterNotTagsResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterOrResult(dict):
    def __init__(
        __self__,
        *,
        cost_category: Optional[outputs.GetTagsFilterOrCostCategoryResult] = ...,
        dimension: Optional[outputs.GetTagsFilterOrDimensionResult] = ...,
        tags: Optional[outputs.GetTagsFilterOrTagsResult] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategory")
    def cost_category(self) -> Optional[outputs.GetTagsFilterOrCostCategoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[outputs.GetTagsFilterOrDimensionResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.GetTagsFilterOrTagsResult]: ...

@pulumi.output_type
class GetTagsFilterOrCostCategoryResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterOrDimensionResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterOrTagsResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsFilterTagsResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        match_options: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchOptions")
    def match_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetTagsSortByResult(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        sort_order: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTagsTimePeriodResult(dict):
    def __init__(__self__, *, end: _builtins.str, start: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.str: ...



import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutomaticShortfallSuppressReasonArgs', 'AutomaticShortfallSuppressReasonArgsDict', 'CatalogClaimsItemArgs', 'CatalogClaimsItemArgsDict', 'CommitmentArgs', 'CommitmentArgsDict', 'ConditionsItemArgs', 'ConditionsItemArgsDict', 'CreditBreakdownItemArgs', 'CreditBreakdownItemArgsDict', 'CreditDimensionArgs', 'CreditDimensionArgsDict', 'CreditPoliciesArgs', 'CreditPoliciesArgsDict', 'CustomPricePropertiesArgs', 'CustomPricePropertiesArgsDict', 'DiscountCustomPriceMultiCurrencyArgs', 'DiscountCustomPriceMultiCurrencyArgsDict', 'DiscountCustomPriceArgs', 'DiscountCustomPriceArgsDict', 'DiscountProductFamilyArgs', 'DiscountProductFamilyArgsDict', 'DiscountProductArgs', 'DiscountProductArgsDict', 'DiscountTypeProductSkuArgs', 'DiscountTypeProductSkuArgsDict', 'EntityTypeAffiliateDiscountArgs', 'EntityTypeAffiliateDiscountArgsDict', 'EntityTypePrimaryDiscountArgs', 'EntityTypePrimaryDiscountArgsDict', 'MaccMilestoneArgs', 'MaccMilestoneArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'MarketSetPricesItemsArgs', 'MarketSetPricesItemsArgsDict', 'PlanArgs', 'PlanArgsDict', 'PriceGuaranteePropertiesArgs', 'PriceGuaranteePropertiesArgsDict', 'PriceArgs', 'PriceArgsDict', 'ShortfallArgs', 'ShortfallArgsDict', 'SkuArgs', 'SkuArgsDict']
class AutomaticShortfallSuppressReasonArgsDict(TypedDict):
    
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AutomaticShortfallSuppressReasonArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogClaimsItemArgsDict(TypedDict):
    
    catalog_claims_item_type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogClaimsItemArgs:
    def __init__(__self__, *, catalog_claims_item_type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogClaimsItemType")
    def catalog_claims_item_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @catalog_claims_item_type.setter
    def catalog_claims_item_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CommitmentArgsDict(TypedDict):
    
    amount: NotRequired[pulumi.Input[_builtins.float]]
    currency_code: NotRequired[pulumi.Input[_builtins.str]]
    grain: NotRequired[pulumi.Input[Union[_builtins.str, CommitmentGrain]]]


@pulumi.input_type
class CommitmentArgs:
    def __init__(__self__, *, amount: Optional[pulumi.Input[_builtins.float]] = ..., currency_code: Optional[pulumi.Input[_builtins.str]] = ..., grain: Optional[pulumi.Input[Union[_builtins.str, CommitmentGrain]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[pulumi.Input[_builtins.float]]:
        ...
    
    @amount.setter
    def amount(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @currency_code.setter
    def currency_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def grain(self) -> Optional[pulumi.Input[Union[_builtins.str, CommitmentGrain]]]:
        
        ...
    
    @grain.setter
    def grain(self, value: Optional[pulumi.Input[Union[_builtins.str, CommitmentGrain]]]): # -> None:
        ...
    


class ConditionsItemArgsDict(TypedDict):
    
    condition_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConditionsItemArgs:
    def __init__(__self__, *, condition_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionName")
    def condition_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @condition_name.setter
    def condition_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def value(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CreditBreakdownItemArgsDict(TypedDict):
    
    allocation: NotRequired[pulumi.Input[CommitmentArgsDict]]
    dimensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CreditDimensionArgsDict]]]]
    end_at: NotRequired[pulumi.Input[_builtins.str]]
    start_at: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CreditBreakdownItemArgs:
    def __init__(__self__, *, allocation: Optional[pulumi.Input[CommitmentArgs]] = ..., dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[CreditDimensionArgs]]]] = ..., end_at: Optional[pulumi.Input[_builtins.str]] = ..., start_at: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allocation(self) -> Optional[pulumi.Input[CommitmentArgs]]:
        
        ...
    
    @allocation.setter
    def allocation(self, value: Optional[pulumi.Input[CommitmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CreditDimensionArgs]]]]:
        
        ...
    
    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CreditDimensionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_at.setter
    def end_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_at.setter
    def start_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CreditDimensionArgsDict(TypedDict):
    
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class CreditDimensionArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CreditPoliciesArgsDict(TypedDict):
    
    expiration: NotRequired[pulumi.Input[Union[_builtins.str, CreditExpirationPolicy]]]
    redemption: NotRequired[pulumi.Input[Union[_builtins.str, CreditRedemptionPolicy]]]


@pulumi.input_type
class CreditPoliciesArgs:
    def __init__(__self__, *, expiration: Optional[pulumi.Input[Union[_builtins.str, CreditExpirationPolicy]]] = ..., redemption: Optional[pulumi.Input[Union[_builtins.str, CreditRedemptionPolicy]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[Union[_builtins.str, CreditExpirationPolicy]]]:
        
        ...
    
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[Union[_builtins.str, CreditExpirationPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redemption(self) -> Optional[pulumi.Input[Union[_builtins.str, CreditRedemptionPolicy]]]:
        
        ...
    
    @redemption.setter
    def redemption(self, value: Optional[pulumi.Input[Union[_builtins.str, CreditRedemptionPolicy]]]): # -> None:
        ...
    


class CustomPricePropertiesArgsDict(TypedDict):
    
    catalog_claims: pulumi.Input[Sequence[pulumi.Input[CatalogClaimsItemArgsDict]]]
    catalog_id: pulumi.Input[_builtins.str]
    market_set_prices: pulumi.Input[Sequence[pulumi.Input[MarketSetPricesItemsArgsDict]]]
    rule_type: pulumi.Input[Union[_builtins.str, DiscountRuleType]]
    billing_period: NotRequired[pulumi.Input[_builtins.str]]
    meter_type: NotRequired[pulumi.Input[_builtins.str]]
    term_units: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomPricePropertiesArgs:
    def __init__(__self__, *, catalog_claims: pulumi.Input[Sequence[pulumi.Input[CatalogClaimsItemArgs]]], catalog_id: pulumi.Input[_builtins.str], market_set_prices: pulumi.Input[Sequence[pulumi.Input[MarketSetPricesItemsArgs]]], rule_type: pulumi.Input[Union[_builtins.str, DiscountRuleType]], billing_period: Optional[pulumi.Input[_builtins.str]] = ..., meter_type: Optional[pulumi.Input[_builtins.str]] = ..., term_units: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogClaims")
    def catalog_claims(self) -> pulumi.Input[Sequence[pulumi.Input[CatalogClaimsItemArgs]]]:
        
        ...
    
    @catalog_claims.setter
    def catalog_claims(self, value: pulumi.Input[Sequence[pulumi.Input[CatalogClaimsItemArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketSetPrices")
    def market_set_prices(self) -> pulumi.Input[Sequence[pulumi.Input[MarketSetPricesItemsArgs]]]:
        
        ...
    
    @market_set_prices.setter
    def market_set_prices(self, value: pulumi.Input[Sequence[pulumi.Input[MarketSetPricesItemsArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[Union[_builtins.str, DiscountRuleType]]:
        
        ...
    
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[Union[_builtins.str, DiscountRuleType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingPeriod")
    def billing_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_period.setter
    def billing_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="meterType")
    def meter_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @meter_type.setter
    def meter_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="termUnits")
    def term_units(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @term_units.setter
    def term_units(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiscountCustomPriceMultiCurrencyArgsDict(TypedDict):
    
    apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]
    discount_type: pulumi.Input[_builtins.str]
    conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgsDict]]]]
    custom_price_properties: NotRequired[pulumi.Input[CustomPricePropertiesArgsDict]]
    discount_combination_rule: NotRequired[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    price_guarantee_properties: NotRequired[pulumi.Input[PriceGuaranteePropertiesArgsDict]]
    product_family_name: NotRequired[pulumi.Input[_builtins.str]]
    product_id: NotRequired[pulumi.Input[_builtins.str]]
    sku_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiscountCustomPriceMultiCurrencyArgs:
    def __init__(__self__, *, apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]], discount_type: pulumi.Input[_builtins.str], conditions: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]] = ..., custom_price_properties: Optional[pulumi.Input[CustomPricePropertiesArgs]] = ..., discount_combination_rule: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., price_guarantee_properties: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]] = ..., product_family_name: Optional[pulumi.Input[_builtins.str]] = ..., product_id: Optional[pulumi.Input[_builtins.str]] = ..., sku_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]:
        
        ...
    
    @apply_discount_on.setter
    def apply_discount_on(self, value: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @discount_type.setter
    def discount_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPriceProperties")
    def custom_price_properties(self) -> Optional[pulumi.Input[CustomPricePropertiesArgs]]:
        
        ...
    
    @custom_price_properties.setter
    def custom_price_properties(self, value: Optional[pulumi.Input[CustomPricePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]:
        
        ...
    
    @discount_combination_rule.setter
    def discount_combination_rule(self, value: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]:
        
        ...
    
    @price_guarantee_properties.setter
    def price_guarantee_properties(self, value: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_family_name.setter
    def product_family_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku_id.setter
    def sku_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiscountCustomPriceArgsDict(TypedDict):
    
    apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]
    discount_type: pulumi.Input[_builtins.str]
    conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgsDict]]]]
    custom_price_properties: NotRequired[pulumi.Input[CustomPricePropertiesArgsDict]]
    discount_combination_rule: NotRequired[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    price_guarantee_properties: NotRequired[pulumi.Input[PriceGuaranteePropertiesArgsDict]]
    product_family_name: NotRequired[pulumi.Input[_builtins.str]]
    product_id: NotRequired[pulumi.Input[_builtins.str]]
    sku_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiscountCustomPriceArgs:
    def __init__(__self__, *, apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]], discount_type: pulumi.Input[_builtins.str], conditions: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]] = ..., custom_price_properties: Optional[pulumi.Input[CustomPricePropertiesArgs]] = ..., discount_combination_rule: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., price_guarantee_properties: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]] = ..., product_family_name: Optional[pulumi.Input[_builtins.str]] = ..., product_id: Optional[pulumi.Input[_builtins.str]] = ..., sku_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]:
        
        ...
    
    @apply_discount_on.setter
    def apply_discount_on(self, value: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @discount_type.setter
    def discount_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPriceProperties")
    def custom_price_properties(self) -> Optional[pulumi.Input[CustomPricePropertiesArgs]]:
        
        ...
    
    @custom_price_properties.setter
    def custom_price_properties(self, value: Optional[pulumi.Input[CustomPricePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]:
        
        ...
    
    @discount_combination_rule.setter
    def discount_combination_rule(self, value: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]:
        
        ...
    
    @price_guarantee_properties.setter
    def price_guarantee_properties(self, value: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_family_name.setter
    def product_family_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku_id.setter
    def sku_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiscountProductFamilyArgsDict(TypedDict):
    
    apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]
    discount_type: pulumi.Input[_builtins.str]
    conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgsDict]]]]
    discount_combination_rule: NotRequired[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    price_guarantee_properties: NotRequired[pulumi.Input[PriceGuaranteePropertiesArgsDict]]
    product_family_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiscountProductFamilyArgs:
    def __init__(__self__, *, apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]], discount_type: pulumi.Input[_builtins.str], conditions: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]] = ..., discount_combination_rule: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., price_guarantee_properties: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]] = ..., product_family_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]:
        
        ...
    
    @apply_discount_on.setter
    def apply_discount_on(self, value: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @discount_type.setter
    def discount_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]:
        
        ...
    
    @discount_combination_rule.setter
    def discount_combination_rule(self, value: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]:
        
        ...
    
    @price_guarantee_properties.setter
    def price_guarantee_properties(self, value: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_family_name.setter
    def product_family_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiscountProductArgsDict(TypedDict):
    
    apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]
    discount_type: pulumi.Input[_builtins.str]
    conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgsDict]]]]
    discount_combination_rule: NotRequired[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    price_guarantee_properties: NotRequired[pulumi.Input[PriceGuaranteePropertiesArgsDict]]
    product_family_name: NotRequired[pulumi.Input[_builtins.str]]
    product_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiscountProductArgs:
    def __init__(__self__, *, apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]], discount_type: pulumi.Input[_builtins.str], conditions: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]] = ..., discount_combination_rule: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., price_guarantee_properties: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]] = ..., product_family_name: Optional[pulumi.Input[_builtins.str]] = ..., product_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]:
        
        ...
    
    @apply_discount_on.setter
    def apply_discount_on(self, value: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @discount_type.setter
    def discount_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]:
        
        ...
    
    @discount_combination_rule.setter
    def discount_combination_rule(self, value: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]:
        
        ...
    
    @price_guarantee_properties.setter
    def price_guarantee_properties(self, value: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_family_name.setter
    def product_family_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiscountTypeProductSkuArgsDict(TypedDict):
    
    apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]
    discount_type: pulumi.Input[_builtins.str]
    conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgsDict]]]]
    discount_combination_rule: NotRequired[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]
    discount_percentage: NotRequired[pulumi.Input[_builtins.float]]
    price_guarantee_properties: NotRequired[pulumi.Input[PriceGuaranteePropertiesArgsDict]]
    product_family_name: NotRequired[pulumi.Input[_builtins.str]]
    product_id: NotRequired[pulumi.Input[_builtins.str]]
    sku_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiscountTypeProductSkuArgs:
    def __init__(__self__, *, apply_discount_on: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]], discount_type: pulumi.Input[_builtins.str], conditions: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]] = ..., discount_combination_rule: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]] = ..., discount_percentage: Optional[pulumi.Input[_builtins.float]] = ..., price_guarantee_properties: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]] = ..., product_family_name: Optional[pulumi.Input[_builtins.str]] = ..., product_id: Optional[pulumi.Input[_builtins.str]] = ..., sku_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]:
        
        ...
    
    @apply_discount_on.setter
    def apply_discount_on(self, value: pulumi.Input[Union[_builtins.str, ApplyDiscountOn]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @discount_type.setter
    def discount_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionsItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]:
        
        ...
    
    @discount_combination_rule.setter
    def discount_combination_rule(self, value: Optional[pulumi.Input[Union[_builtins.str, DiscountCombinationRule]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @discount_percentage.setter
    def discount_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]:
        
        ...
    
    @price_guarantee_properties.setter
    def price_guarantee_properties(self, value: Optional[pulumi.Input[PriceGuaranteePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_family_name.setter
    def product_family_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku_id.setter
    def sku_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EntityTypeAffiliateDiscountArgsDict(TypedDict):
    
    entity_type: pulumi.Input[_builtins.str]
    product_code: pulumi.Input[_builtins.str]
    start_at: pulumi.Input[_builtins.str]
    applied_scope_type: NotRequired[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    system_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EntityTypeAffiliateDiscountArgs:
    def __init__(__self__, *, entity_type: pulumi.Input[_builtins.str], product_code: pulumi.Input[_builtins.str], start_at: pulumi.Input[_builtins.str], applied_scope_type: Optional[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., system_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @product_code.setter
    def product_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @start_at.setter
    def start_at(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedScopeType")
    def applied_scope_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]]:
        
        ...
    
    @applied_scope_type.setter
    def applied_scope_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @system_id.setter
    def system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EntityTypePrimaryDiscountArgsDict(TypedDict):
    
    end_at: pulumi.Input[_builtins.str]
    entity_type: pulumi.Input[_builtins.str]
    product_code: pulumi.Input[_builtins.str]
    start_at: pulumi.Input[_builtins.str]
    applied_scope_type: NotRequired[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]]
    discount_type_properties: NotRequired[pulumi.Input[Union[DiscountCustomPriceArgsDict, DiscountCustomPriceMultiCurrencyArgsDict, DiscountProductArgsDict, DiscountProductFamilyArgsDict, DiscountTypeProductSkuArgsDict]]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    system_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EntityTypePrimaryDiscountArgs:
    def __init__(__self__, *, end_at: pulumi.Input[_builtins.str], entity_type: pulumi.Input[_builtins.str], product_code: pulumi.Input[_builtins.str], start_at: pulumi.Input[_builtins.str], applied_scope_type: Optional[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]] = ..., discount_type_properties: Optional[pulumi.Input[Union[DiscountCustomPriceArgs, DiscountCustomPriceMultiCurrencyArgs, DiscountProductArgs, DiscountProductFamilyArgs, DiscountTypeProductSkuArgs]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., system_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @end_at.setter
    def end_at(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @product_code.setter
    def product_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @start_at.setter
    def start_at(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedScopeType")
    def applied_scope_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]]:
        
        ...
    
    @applied_scope_type.setter
    def applied_scope_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiscountAppliedScopeType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountTypeProperties")
    def discount_type_properties(self) -> Optional[pulumi.Input[Union[DiscountCustomPriceArgs, DiscountCustomPriceMultiCurrencyArgs, DiscountProductArgs, DiscountProductFamilyArgs, DiscountTypeProductSkuArgs]]]:
        
        ...
    
    @discount_type_properties.setter
    def discount_type_properties(self, value: Optional[pulumi.Input[Union[DiscountCustomPriceArgs, DiscountCustomPriceMultiCurrencyArgs, DiscountProductArgs, DiscountProductFamilyArgs, DiscountTypeProductSkuArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @system_id.setter
    def system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MaccMilestoneArgsDict(TypedDict):
    
    automatic_shortfall: NotRequired[pulumi.Input[Union[_builtins.str, EnablementMode]]]
    automatic_shortfall_suppress_reason: NotRequired[pulumi.Input[AutomaticShortfallSuppressReasonArgsDict]]
    commitment: NotRequired[pulumi.Input[PriceArgsDict]]
    end_at: NotRequired[pulumi.Input[_builtins.str]]
    milestone_id: NotRequired[pulumi.Input[_builtins.str]]
    shortfall: NotRequired[pulumi.Input[ShortfallArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, MaccMilestoneStatus]]]


@pulumi.input_type
class MaccMilestoneArgs:
    def __init__(__self__, *, automatic_shortfall: Optional[pulumi.Input[Union[_builtins.str, EnablementMode]]] = ..., automatic_shortfall_suppress_reason: Optional[pulumi.Input[AutomaticShortfallSuppressReasonArgs]] = ..., commitment: Optional[pulumi.Input[PriceArgs]] = ..., end_at: Optional[pulumi.Input[_builtins.str]] = ..., milestone_id: Optional[pulumi.Input[_builtins.str]] = ..., shortfall: Optional[pulumi.Input[ShortfallArgs]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, MaccMilestoneStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticShortfall")
    def automatic_shortfall(self) -> Optional[pulumi.Input[Union[_builtins.str, EnablementMode]]]:
        
        ...
    
    @automatic_shortfall.setter
    def automatic_shortfall(self, value: Optional[pulumi.Input[Union[_builtins.str, EnablementMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticShortfallSuppressReason")
    def automatic_shortfall_suppress_reason(self) -> Optional[pulumi.Input[AutomaticShortfallSuppressReasonArgs]]:
        
        ...
    
    @automatic_shortfall_suppress_reason.setter
    def automatic_shortfall_suppress_reason(self, value: Optional[pulumi.Input[AutomaticShortfallSuppressReasonArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> Optional[pulumi.Input[PriceArgs]]:
        
        ...
    
    @commitment.setter
    def commitment(self, value: Optional[pulumi.Input[PriceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_at.setter
    def end_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="milestoneId")
    def milestone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @milestone_id.setter
    def milestone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def shortfall(self) -> Optional[pulumi.Input[ShortfallArgs]]:
        
        ...
    
    @shortfall.setter
    def shortfall(self, value: Optional[pulumi.Input[ShortfallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, MaccMilestoneStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, MaccMilestoneStatus]]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MarketSetPricesItemsArgsDict(TypedDict):
    
    currency: pulumi.Input[_builtins.str]
    markets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    value: pulumi.Input[_builtins.float]


@pulumi.input_type
class MarketSetPricesItemsArgs:
    def __init__(__self__, *, currency: pulumi.Input[_builtins.str], markets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], value: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @currency.setter
    def currency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def markets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        ...
    
    @markets.setter
    def markets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class PlanArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    product: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PlanArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], product: pulumi.Input[_builtins.str], publisher: pulumi.Input[_builtins.str], promotion_code: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @product.setter
    def product(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PriceGuaranteePropertiesArgsDict(TypedDict):
    
    price_guarantee_date: NotRequired[pulumi.Input[_builtins.str]]
    pricing_policy: NotRequired[pulumi.Input[Union[_builtins.str, PricingPolicy]]]


@pulumi.input_type
class PriceGuaranteePropertiesArgs:
    def __init__(__self__, *, price_guarantee_date: Optional[pulumi.Input[_builtins.str]] = ..., pricing_policy: Optional[pulumi.Input[Union[_builtins.str, PricingPolicy]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeDate")
    def price_guarantee_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @price_guarantee_date.setter
    def price_guarantee_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingPolicy")
    def pricing_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, PricingPolicy]]]:
        
        ...
    
    @pricing_policy.setter
    def pricing_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, PricingPolicy]]]): # -> None:
        ...
    


class PriceArgsDict(TypedDict):
    amount: NotRequired[pulumi.Input[_builtins.float]]
    currency_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PriceArgs:
    def __init__(__self__, *, amount: Optional[pulumi.Input[_builtins.float]] = ..., currency_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[pulumi.Input[_builtins.float]]:
        ...
    
    @amount.setter
    def amount(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @currency_code.setter
    def currency_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ShortfallArgsDict(TypedDict):
    
    balance_version: NotRequired[pulumi.Input[_builtins.float]]
    charge: NotRequired[pulumi.Input[CommitmentArgsDict]]
    end_at: NotRequired[pulumi.Input[_builtins.str]]
    product_code: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    start_at: NotRequired[pulumi.Input[_builtins.str]]
    system_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ShortfallArgs:
    def __init__(__self__, *, balance_version: Optional[pulumi.Input[_builtins.float]] = ..., charge: Optional[pulumi.Input[CommitmentArgs]] = ..., end_at: Optional[pulumi.Input[_builtins.str]] = ..., product_code: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., start_at: Optional[pulumi.Input[_builtins.str]] = ..., system_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="balanceVersion")
    def balance_version(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @balance_version.setter
    def balance_version(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def charge(self) -> Optional[pulumi.Input[CommitmentArgs]]:
        
        ...
    
    @charge.setter
    def charge(self, value: Optional[pulumi.Input[CommitmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_at.setter
    def end_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_code.setter
    def product_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_at.setter
    def start_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @system_id.setter
    def system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[SkuTier]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): # -> None:
        ...
    



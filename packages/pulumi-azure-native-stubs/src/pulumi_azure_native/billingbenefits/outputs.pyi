

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutomaticShortfallSuppressReasonResponse', 'CatalogClaimsItemResponse', 'CommitmentResponse', 'ConditionsItemResponse', 'CreditBreakdownItemResponse', 'CreditDimensionResponse', 'CreditPoliciesResponse', 'CreditReasonResponse', 'CustomPricePropertiesResponse', 'DiscountCustomPriceMultiCurrencyResponse', 'DiscountCustomPriceResponse', 'DiscountProductFamilyResponse', 'DiscountProductResponse', 'DiscountTypeProductSkuResponse', 'EntityTypeAffiliateDiscountResponse', 'EntityTypePrimaryDiscountResponse', 'MaccMilestoneResponse', 'ManagedServiceIdentityResponse', 'MarketSetPricesItemsResponse', 'PlanResponse', 'PriceGuaranteePropertiesResponse', 'PriceResponse', 'ShortfallResponse', 'SkuResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse']
@pulumi.output_type
class AutomaticShortfallSuppressReasonResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CatalogClaimsItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, catalog_claims_item_type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogClaimsItemType")
    def catalog_claims_item_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class CommitmentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amount: Optional[_builtins.float] = ..., currency_code: Optional[_builtins.str] = ..., grain: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grain(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConditionsItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., value: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionName")
    def condition_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class CreditBreakdownItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocation: Optional[outputs.CommitmentResponse] = ..., dimensions: Optional[Sequence[outputs.CreditDimensionResponse]] = ..., end_at: Optional[_builtins.str] = ..., start_at: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allocation(self) -> Optional[outputs.CommitmentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.CreditDimensionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CreditDimensionResponse(dict):
    
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CreditPoliciesResponse(dict):
    
    def __init__(__self__, *, expiration: Optional[_builtins.str] = ..., redemption: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def redemption(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CreditReasonResponse(dict):
    
    def __init__(__self__, *, code: _builtins.float, description: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CustomPricePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, catalog_claims: Sequence[outputs.CatalogClaimsItemResponse], catalog_id: _builtins.str, market_set_prices: Sequence[outputs.MarketSetPricesItemsResponse], rule_type: _builtins.str, billing_period: Optional[_builtins.str] = ..., meter_type: Optional[_builtins.str] = ..., term_units: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogClaims")
    def catalog_claims(self) -> Sequence[outputs.CatalogClaimsItemResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketSetPrices")
    def market_set_prices(self) -> Sequence[outputs.MarketSetPricesItemsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingPeriod")
    def billing_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="meterType")
    def meter_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="termUnits")
    def term_units(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiscountCustomPriceMultiCurrencyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, apply_discount_on: _builtins.str, discount_type: _builtins.str, conditions: Optional[Sequence[outputs.ConditionsItemResponse]] = ..., custom_price_properties: Optional[outputs.CustomPricePropertiesResponse] = ..., discount_combination_rule: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., price_guarantee_properties: Optional[outputs.PriceGuaranteePropertiesResponse] = ..., product_family_name: Optional[_builtins.str] = ..., product_id: Optional[_builtins.str] = ..., sku_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.ConditionsItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPriceProperties")
    def custom_price_properties(self) -> Optional[outputs.CustomPricePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[outputs.PriceGuaranteePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiscountCustomPriceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, apply_discount_on: _builtins.str, discount_type: _builtins.str, conditions: Optional[Sequence[outputs.ConditionsItemResponse]] = ..., custom_price_properties: Optional[outputs.CustomPricePropertiesResponse] = ..., discount_combination_rule: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., price_guarantee_properties: Optional[outputs.PriceGuaranteePropertiesResponse] = ..., product_family_name: Optional[_builtins.str] = ..., product_id: Optional[_builtins.str] = ..., sku_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.ConditionsItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPriceProperties")
    def custom_price_properties(self) -> Optional[outputs.CustomPricePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[outputs.PriceGuaranteePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiscountProductFamilyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, apply_discount_on: _builtins.str, discount_type: _builtins.str, conditions: Optional[Sequence[outputs.ConditionsItemResponse]] = ..., discount_combination_rule: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., price_guarantee_properties: Optional[outputs.PriceGuaranteePropertiesResponse] = ..., product_family_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.ConditionsItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[outputs.PriceGuaranteePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiscountProductResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, apply_discount_on: _builtins.str, discount_type: _builtins.str, conditions: Optional[Sequence[outputs.ConditionsItemResponse]] = ..., discount_combination_rule: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., price_guarantee_properties: Optional[outputs.PriceGuaranteePropertiesResponse] = ..., product_family_name: Optional[_builtins.str] = ..., product_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.ConditionsItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[outputs.PriceGuaranteePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiscountTypeProductSkuResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, apply_discount_on: _builtins.str, discount_type: _builtins.str, conditions: Optional[Sequence[outputs.ConditionsItemResponse]] = ..., discount_combination_rule: Optional[_builtins.str] = ..., discount_percentage: Optional[_builtins.float] = ..., price_guarantee_properties: Optional[outputs.PriceGuaranteePropertiesResponse] = ..., product_family_name: Optional[_builtins.str] = ..., product_id: Optional[_builtins.str] = ..., sku_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDiscountOn")
    def apply_discount_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountType")
    def discount_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.ConditionsItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountCombinationRule")
    def discount_combination_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeProperties")
    def price_guarantee_properties(self) -> Optional[outputs.PriceGuaranteePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EntityTypeAffiliateDiscountResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, benefit_resource_id: _builtins.str, billing_account_resource_id: _builtins.str, billing_profile_resource_id: _builtins.str, customer_resource_id: _builtins.str, end_at: _builtins.str, entity_type: _builtins.str, primary_resource_id: _builtins.str, product_code: _builtins.str, provisioning_state: _builtins.str, start_at: _builtins.str, status: _builtins.str, applied_scope_type: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., system_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="benefitResourceId")
    def benefit_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountResourceId")
    def billing_account_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProfileResourceId")
    def billing_profile_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerResourceId")
    def customer_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryResourceId")
    def primary_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedScopeType")
    def applied_scope_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EntityTypePrimaryDiscountResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, benefit_resource_id: _builtins.str, billing_account_resource_id: _builtins.str, billing_profile_resource_id: _builtins.str, customer_resource_id: _builtins.str, end_at: _builtins.str, entity_type: _builtins.str, product_code: _builtins.str, provisioning_state: _builtins.str, start_at: _builtins.str, status: _builtins.str, applied_scope_type: Optional[_builtins.str] = ..., discount_type_properties: Optional[Any] = ..., display_name: Optional[_builtins.str] = ..., system_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="benefitResourceId")
    def benefit_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountResourceId")
    def billing_account_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProfileResourceId")
    def billing_profile_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerResourceId")
    def customer_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedScopeType")
    def applied_scope_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discountTypeProperties")
    def discount_type_properties(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MaccMilestoneResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic_shortfall: Optional[_builtins.str] = ..., automatic_shortfall_suppress_reason: Optional[outputs.AutomaticShortfallSuppressReasonResponse] = ..., commitment: Optional[outputs.PriceResponse] = ..., end_at: Optional[_builtins.str] = ..., milestone_id: Optional[_builtins.str] = ..., shortfall: Optional[outputs.ShortfallResponse] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticShortfall")
    def automatic_shortfall(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticShortfallSuppressReason")
    def automatic_shortfall_suppress_reason(self) -> Optional[outputs.AutomaticShortfallSuppressReasonResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> Optional[outputs.PriceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="milestoneId")
    def milestone_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shortfall(self) -> Optional[outputs.ShortfallResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class MarketSetPricesItemsResponse(dict):
    
    def __init__(__self__, *, currency: _builtins.str, markets: Sequence[_builtins.str], value: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def markets(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class PlanResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, product: _builtins.str, publisher: _builtins.str, promotion_code: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PriceGuaranteePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, price_guarantee_date: Optional[_builtins.str] = ..., pricing_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priceGuaranteeDate")
    def price_guarantee_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingPolicy")
    def pricing_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PriceResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amount: Optional[_builtins.float] = ..., currency_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ShortfallResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, balance_version: Optional[_builtins.float] = ..., charge: Optional[outputs.CommitmentResponse] = ..., end_at: Optional[_builtins.str] = ..., product_code: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., start_at: Optional[_builtins.str] = ..., system_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="balanceVersion")
    def balance_version(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def charge(self) -> Optional[outputs.CommitmentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    



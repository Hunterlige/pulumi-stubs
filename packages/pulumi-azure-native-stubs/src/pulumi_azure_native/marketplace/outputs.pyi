

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NewNotificationsResponse', 'PlanNotificationDetailsResponse', 'PlanResponse', 'ProductResponse', 'RuleResponse', ..., 'SystemDataResponse']
@pulumi.output_type
class NewNotificationsResponse(dict):
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., icon: Optional[_builtins.str] = ..., is_future_plans_enabled: Optional[_builtins.bool] = ..., message_code: Optional[_builtins.float] = ..., offer_id: Optional[_builtins.str] = ..., plans: Optional[Sequence[outputs.PlanNotificationDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFuturePlansEnabled")
    def is_future_plans_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageCode")
    def message_code(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plans(self) -> Optional[Sequence[outputs.PlanNotificationDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class PlanNotificationDetailsResponse(dict):
    
    def __init__(__self__, *, plan_display_name: Optional[_builtins.str] = ..., plan_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planDisplayName")
    def plan_display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PlanResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alt_stack_reference: _builtins.str, plan_display_name: _builtins.str, plan_id: _builtins.str, sku_id: _builtins.str, stack_type: _builtins.str, accessibility: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="altStackReference")
    def alt_stack_reference(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planDisplayName")
    def plan_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accessibility(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProductResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., pricing_types: Optional[Sequence[_builtins.str]] = ..., product_type: Optional[_builtins.str] = ..., publisher_display_name: Optional[_builtins.str] = ..., rating_average: Optional[_builtins.float] = ..., small_icon_uri: Optional[_builtins.str] = ..., store_fronts: Optional[Sequence[_builtins.str]] = ..., summary: Optional[_builtins.str] = ..., unique_product_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingTypes")
    def pricing_types(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ratingAverage")
    def rating_average(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smallIconUri")
    def small_icon_uri(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storeFronts")
    def store_fronts(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueProductId")
    def unique_product_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleResponse(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ..., value: Optional[Sequence[_builtins.str]] = ...) -> None:
        
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
class StopSellOffersPlansNotificationsListPropertiesResponse(dict):
    
    def __init__(__self__, *, display_name: _builtins.str, icon: _builtins.str, is_entire: _builtins.bool, message_code: _builtins.float, offer_id: _builtins.str, plans: Sequence[outputs.PlanNotificationDetailsResponse], public_context: _builtins.bool, subscriptions_ids: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def icon(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEntire")
    def is_entire(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageCode")
    def message_code(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plans(self) -> Sequence[outputs.PlanNotificationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicContext")
    def public_context(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionsIds")
    def subscriptions_ids(self) -> Sequence[_builtins.str]:
        
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
    



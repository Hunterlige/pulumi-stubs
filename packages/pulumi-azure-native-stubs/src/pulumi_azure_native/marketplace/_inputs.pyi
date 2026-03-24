

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PlanArgs', 'PlanArgsDict', 'ProductArgs', 'ProductArgsDict']
class PlanArgsDict(TypedDict):
    accessibility: NotRequired[pulumi.Input[Union[_builtins.str, Accessibility]]]


@pulumi.input_type
class PlanArgs:
    def __init__(__self__, *, accessibility: Optional[pulumi.Input[Union[_builtins.str, Accessibility]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accessibility(self) -> Optional[pulumi.Input[Union[_builtins.str, Accessibility]]]:
        
        ...
    
    @accessibility.setter
    def accessibility(self, value: Optional[pulumi.Input[Union[_builtins.str, Accessibility]]]): # -> None:
        ...
    


class ProductArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    pricing_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    product_type: NotRequired[pulumi.Input[_builtins.str]]
    publisher_display_name: NotRequired[pulumi.Input[_builtins.str]]
    rating_average: NotRequired[pulumi.Input[_builtins.float]]
    small_icon_uri: NotRequired[pulumi.Input[_builtins.str]]
    store_fronts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    summary: NotRequired[pulumi.Input[_builtins.str]]
    unique_product_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProductArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., pricing_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., product_type: Optional[pulumi.Input[_builtins.str]] = ..., publisher_display_name: Optional[pulumi.Input[_builtins.str]] = ..., rating_average: Optional[pulumi.Input[_builtins.float]] = ..., small_icon_uri: Optional[pulumi.Input[_builtins.str]] = ..., store_fronts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., summary: Optional[pulumi.Input[_builtins.str]] = ..., unique_product_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingTypes")
    def pricing_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @pricing_types.setter
    def pricing_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @product_type.setter
    def product_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @publisher_display_name.setter
    def publisher_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ratingAverage")
    def rating_average(self) -> Optional[pulumi.Input[_builtins.float]]:
        ...
    
    @rating_average.setter
    def rating_average(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smallIconUri")
    def small_icon_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @small_icon_uri.setter
    def small_icon_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storeFronts")
    def store_fronts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @store_fronts.setter
    def store_fronts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @summary.setter
    def summary(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueProductId")
    def unique_product_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @unique_product_id.setter
    def unique_product_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



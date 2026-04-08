import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProfessionalServiceCreationPropertiesArgs",
    "ProfessionalServiceCreationPropertiesArgsDict",
]

class ProfessionalServiceCreationPropertiesArgsDict(TypedDict):
    auto_renew: NotRequired[pulumi.Input[_builtins.bool]]
    billing_period: NotRequired[pulumi.Input[_builtins.str]]
    offer_id: NotRequired[pulumi.Input[_builtins.str]]
    publisher_id: NotRequired[pulumi.Input[_builtins.str]]
    quote_id: NotRequired[pulumi.Input[_builtins.str]]
    sku_id: NotRequired[pulumi.Input[_builtins.str]]
    store_front: NotRequired[pulumi.Input[_builtins.str]]
    term_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProfessionalServiceCreationPropertiesArgs:
    def __init__(
        __self__,
        *,
        auto_renew: Optional[pulumi.Input[_builtins.bool]] = ...,
        billing_period: Optional[pulumi.Input[_builtins.str]] = ...,
        offer_id: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher_id: Optional[pulumi.Input[_builtins.str]] = ...,
        quote_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku_id: Optional[pulumi.Input[_builtins.str]] = ...,
        store_front: Optional[pulumi.Input[_builtins.str]] = ...,
        term_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="billingPeriod")
    def billing_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_period.setter
    def billing_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offer_id.setter
    def offer_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher_id.setter
    def publisher_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quoteId")
    def quote_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quote_id.setter
    def quote_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_id.setter
    def sku_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storeFront")
    def store_front(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @store_front.setter
    def store_front(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @term_unit.setter
    def term_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

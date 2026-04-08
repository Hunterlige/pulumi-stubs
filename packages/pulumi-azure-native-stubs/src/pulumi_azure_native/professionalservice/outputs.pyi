import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProfessionalServicePropertiesResponseTerm",
    "ProfessionalServiceResourceResponseProperties",
]

@pulumi.output_type
class ProfessionalServicePropertiesResponseTerm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_date: Optional[_builtins.str] = ...,
        start_date: Optional[_builtins.str] = ...,
        term_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProfessionalServiceResourceResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created: _builtins.str,
        auto_renew: Optional[_builtins.bool] = ...,
        billing_period: Optional[_builtins.str] = ...,
        is_free_trial: Optional[_builtins.bool] = ...,
        last_modified: Optional[_builtins.str] = ...,
        offer_id: Optional[_builtins.str] = ...,
        payment_channel_metadata: Optional[Mapping[str, _builtins.str]] = ...,
        payment_channel_type: Optional[_builtins.str] = ...,
        publisher_id: Optional[_builtins.str] = ...,
        quote_id: Optional[_builtins.str] = ...,
        sku_id: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        store_front: Optional[_builtins.str] = ...,
        term: Optional[outputs.ProfessionalServicePropertiesResponseTerm] = ...,
        term_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="billingPeriod")
    def billing_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isFreeTrial")
    def is_free_trial(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="paymentChannelMetadata")
    def payment_channel_metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="paymentChannelType")
    def payment_channel_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quoteId")
    def quote_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storeFront")
    def store_front(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def term(self) -> Optional[outputs.ProfessionalServicePropertiesResponseTerm]: ...
    @_builtins.property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> Optional[_builtins.str]: ...

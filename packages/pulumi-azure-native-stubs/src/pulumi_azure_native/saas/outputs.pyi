import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SaasPropertiesResponseTerm", "SaasResourceResponseProperties"]

@pulumi.output_type
class SaasPropertiesResponseTerm(dict):
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
class SaasResourceResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created: _builtins.str,
        auto_renew: Optional[_builtins.bool] = ...,
        is_free_trial: Optional[_builtins.bool] = ...,
        last_modified: Optional[_builtins.str] = ...,
        offer_id: Optional[_builtins.str] = ...,
        payment_channel_metadata: Optional[Mapping[str, _builtins.str]] = ...,
        payment_channel_type: Optional[_builtins.str] = ...,
        publisher_id: Optional[_builtins.str] = ...,
        publisher_test_environment: Optional[_builtins.str] = ...,
        quantity: Optional[_builtins.float] = ...,
        saas_resource_name: Optional[_builtins.str] = ...,
        saas_session_id: Optional[_builtins.str] = ...,
        saas_subscription_id: Optional[_builtins.str] = ...,
        sku_id: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        term: Optional[outputs.SaasPropertiesResponseTerm] = ...,
        term_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[_builtins.bool]: ...
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
    @pulumi.getter(name="publisherTestEnvironment")
    def publisher_test_environment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="saasResourceName")
    def saas_resource_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="saasSessionId")
    def saas_session_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionId")
    def saas_subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def term(self) -> Optional[outputs.SaasPropertiesResponseTerm]: ...
    @_builtins.property
    @pulumi.getter(name="termId")
    def term_id(self) -> Optional[_builtins.str]: ...

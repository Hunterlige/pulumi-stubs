import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrivateStoreCollectionOfferResult",
    "AwaitableGetPrivateStoreCollectionOfferResult",
    "get_private_store_collection_offer",
    "get_private_store_collection_offer_output",
]

@pulumi.output_type
class GetPrivateStoreCollectionOfferResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_at=...,
        e_tag=...,
        icon_file_uris=...,
        id=...,
        modified_at=...,
        name=...,
        offer_display_name=...,
        plans=...,
        private_store_id=...,
        publisher_display_name=...,
        specific_plan_ids_limitation=...,
        system_data=...,
        type=...,
        unique_offer_id=...,
        update_suppressed_due_idempotence=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconFileUris")
    def icon_file_uris(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offerDisplayName")
    def offer_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def plans(self) -> Optional[Sequence[outputs.PlanResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateStoreId")
    def private_store_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="specificPlanIdsLimitation")
    def specific_plan_ids_limitation(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueOfferId")
    def unique_offer_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateSuppressedDueIdempotence")
    def update_suppressed_due_idempotence(self) -> Optional[_builtins.bool]: ...

class AwaitableGetPrivateStoreCollectionOfferResult(
    GetPrivateStoreCollectionOfferResult
):
    def __await__(self): ...

def get_private_store_collection_offer(
    collection_id: Optional[_builtins.str] = ...,
    offer_id: Optional[_builtins.str] = ...,
    private_store_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrivateStoreCollectionOfferResult: ...
def get_private_store_collection_offer_output(
    collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    offer_id: Optional[pulumi.Input[_builtins.str]] = ...,
    private_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrivateStoreCollectionOfferResult]: ...

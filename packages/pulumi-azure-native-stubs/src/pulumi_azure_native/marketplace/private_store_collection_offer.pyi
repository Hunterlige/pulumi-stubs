import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrivateStoreCollectionOfferArgs", "PrivateStoreCollectionOffer"]

@pulumi.input_type
class PrivateStoreCollectionOfferArgs:
    def __init__(
        __self__,
        *,
        collection_id: pulumi.Input[_builtins.str],
        private_store_id: pulumi.Input[_builtins.str],
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        icon_file_uris: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        offer_id: Optional[pulumi.Input[_builtins.str]] = ...,
        plans: Optional[pulumi.Input[Sequence[pulumi.Input[PlanArgs]]]] = ...,
        specific_plan_ids_limitation: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        update_suppressed_due_idempotence: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[_builtins.str]: ...
    @collection_id.setter
    def collection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateStoreId")
    def private_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @private_store_id.setter
    def private_store_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iconFileUris")
    def icon_file_uris(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @icon_file_uris.setter
    def icon_file_uris(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offer_id.setter
    def offer_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def plans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanArgs]]]]: ...
    @plans.setter
    def plans(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="specificPlanIdsLimitation")
    def specific_plan_ids_limitation(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @specific_plan_ids_limitation.setter
    def specific_plan_ids_limitation(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateSuppressedDueIdempotence")
    def update_suppressed_due_idempotence(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @update_suppressed_due_idempotence.setter
    def update_suppressed_due_idempotence(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token(...)
class PrivateStoreCollectionOffer(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        icon_file_uris: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        offer_id: Optional[pulumi.Input[_builtins.str]] = ...,
        plans: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[PlanArgs, PlanArgsDict]]]]
        ] = ...,
        private_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        specific_plan_ids_limitation: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        update_suppressed_due_idempotence: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrivateStoreCollectionOfferArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PrivateStoreCollectionOffer: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="iconFileUris")
    def icon_file_uris(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offerDisplayName")
    def offer_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plans(self) -> pulumi.Output[Optional[Sequence[outputs.PlanResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="privateStoreId")
    def private_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="specificPlanIdsLimitation")
    def specific_plan_ids_limitation(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueOfferId")
    def unique_offer_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateSuppressedDueIdempotence")
    def update_suppressed_due_idempotence(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...

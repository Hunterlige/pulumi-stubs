import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProductResult",
    "AwaitableGetProductResult",
    "get_product",
    "get_product_output",
]

@pulumi.output_type
class GetProductResult:
    def __init__(
        __self__,
        billing_part_number=...,
        compatibility=...,
        description=...,
        display_name=...,
        etag=...,
        gallery_item_identity=...,
        icon_uris=...,
        id=...,
        legal_terms=...,
        links=...,
        name=...,
        offer=...,
        offer_version=...,
        payload_length=...,
        privacy_policy=...,
        product_kind=...,
        product_properties=...,
        publisher_display_name=...,
        publisher_identifier=...,
        sku=...,
        type=...,
        vm_extension_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingPartNumber")
    def billing_part_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compatibility(self) -> Optional[outputs.CompatibilityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="galleryItemIdentity")
    def gallery_item_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconUris")
    def icon_uris(self) -> Optional[outputs.IconUrisResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="legalTerms")
    def legal_terms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[Sequence[outputs.ProductLinkResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offerVersion")
    def offer_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="payloadLength")
    def payload_length(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="privacyPolicy")
    def privacy_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productKind")
    def product_kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productProperties")
    def product_properties(self) -> Optional[outputs.ProductPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publisherIdentifier")
    def publisher_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmExtensionType")
    def vm_extension_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetProductResult(GetProductResult):
    def __await__(self): ...

def get_product(
    product_name: Optional[_builtins.str] = ...,
    registration_name: Optional[_builtins.str] = ...,
    resource_group: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProductResult: ...
def get_product_output(
    product_name: Optional[pulumi.Input[_builtins.str]] = ...,
    registration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProductResult]: ...

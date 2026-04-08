import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CompatibilityResponse",
    "DataDiskImageResponse",
    "IconUrisResponse",
    "OsDiskImageResponse",
    "ProductLinkResponse",
    "ProductPropertiesResponse",
    "ProductResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class CompatibilityResponse(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        is_compatible: Optional[_builtins.bool] = ...,
        issues: Optional[Sequence[_builtins.str]] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isCompatible")
    def is_compatible(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def issues(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataDiskImageResponse(dict):
    def __init__(
        __self__, *, lun: _builtins.int, source_blob_sas_uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sourceBlobSasUri")
    def source_blob_sas_uri(self) -> _builtins.str: ...

@pulumi.output_type
class IconUrisResponse(dict):
    def __init__(
        __self__,
        *,
        hero: Optional[_builtins.str] = ...,
        large: Optional[_builtins.str] = ...,
        medium: Optional[_builtins.str] = ...,
        small: Optional[_builtins.str] = ...,
        wide: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hero(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def large(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def small(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def wide(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsDiskImageResponse(dict):
    def __init__(
        __self__, *, operating_system: _builtins.str, source_blob_sas_uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceBlobSasUri")
    def source_blob_sas_uri(self) -> _builtins.str: ...

@pulumi.output_type
class ProductLinkResponse(dict):
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProductPropertiesResponse(dict):
    def __init__(__self__, *, version: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProductResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        billing_part_number: Optional[_builtins.str] = ...,
        compatibility: Optional[outputs.CompatibilityResponse] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        etag: Optional[_builtins.str] = ...,
        gallery_item_identity: Optional[_builtins.str] = ...,
        icon_uris: Optional[outputs.IconUrisResponse] = ...,
        legal_terms: Optional[_builtins.str] = ...,
        links: Optional[Sequence[outputs.ProductLinkResponse]] = ...,
        offer: Optional[_builtins.str] = ...,
        offer_version: Optional[_builtins.str] = ...,
        payload_length: Optional[_builtins.float] = ...,
        privacy_policy: Optional[_builtins.str] = ...,
        product_kind: Optional[_builtins.str] = ...,
        product_properties: Optional[outputs.ProductPropertiesResponse] = ...,
        publisher_display_name: Optional[_builtins.str] = ...,
        publisher_identifier: Optional[_builtins.str] = ...,
        sku: Optional[_builtins.str] = ...,
        vm_extension_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
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
    @pulumi.getter(name="legalTerms")
    def legal_terms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[Sequence[outputs.ProductLinkResponse]]: ...
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
    @pulumi.getter(name="vmExtensionType")
    def vm_extension_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

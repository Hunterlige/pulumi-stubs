import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdditionalConfigurationResponse",
    "AddressDetailsResponse",
    "AddressPropertiesResponse",
    "AvailabilityInformationResponse",
    "BillingMeterDetailsResponse",
    "CategoryInformationResponse",
    "ChildConfigurationResponse",
    "ConfigurationDeviceDetailsResponse",
    "ConfigurationResponse",
    "ContactDetailsResponse",
    "CostInformationResponse",
    "DescriptionResponse",
    "DeviceDetailsResponse",
    "DevicePresenceVerificationDetailsResponse",
    "DimensionsResponse",
    "DisplayInfoResponse",
    "EncryptionPreferencesResponse",
    "ErrorAdditionalInfoResponse",
    "ErrorDetailResponse",
    "FilterablePropertyResponse",
    "ForwardShippingDetailsResponse",
    "GroupedChildConfigurationsResponse",
    "HierarchyInformationResponse",
    "ImageInformationResponse",
    "LinkResponse",
    "ManagementResourcePreferencesResponse",
    "NotificationPreferenceResponse",
    "OrderItemDetailsResponse",
    "Pav2MeterDetailsResponse",
    "PreferencesResponse",
    "ProductDetailsResponse",
    "ProductFamilyResponse",
    "ProductLineResponse",
    "ProductResponse",
    "ProvisioningDetailsResponse",
    "PurchaseMeterDetailsResponse",
    "ResourceIdentityResponse",
    "ResourceProviderDetailsResponse",
    "ReverseShippingDetailsResponse",
    "ShippingAddressResponse",
    "SiteDetailsResponse",
    "SpecificationResponse",
    "StageDetailsResponse",
    "SystemDataResponse",
    "TermCommitmentInformationResponse",
    "TermCommitmentPreferencesResponse",
    "TermTypeDetailsResponse",
    "TransportPreferencesResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class AdditionalConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hierarchy_information: outputs.HierarchyInformationResponse,
        quantity: _builtins.int,
        provisioning_details: Optional[
            Sequence[outputs.ProvisioningDetailsResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisioningDetails")
    def provisioning_details(
        self,
    ) -> Optional[Sequence[outputs.ProvisioningDetailsResponse]]: ...

@pulumi.output_type
class AddressDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        forward_address: outputs.AddressPropertiesResponse,
        return_address: outputs.AddressPropertiesResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="forwardAddress")
    def forward_address(self) -> outputs.AddressPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="returnAddress")
    def return_address(self) -> outputs.AddressPropertiesResponse: ...

@pulumi.output_type
class AddressPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_validation_status: _builtins.str,
        provisioning_state: _builtins.str,
        address_classification: Optional[_builtins.str] = ...,
        contact_details: Optional[outputs.ContactDetailsResponse] = ...,
        shipping_address: Optional[outputs.ShippingAddressResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressValidationStatus")
    def address_validation_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressClassification")
    def address_classification(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> Optional[outputs.ContactDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[outputs.ShippingAddressResponse]: ...

@pulumi.output_type
class AvailabilityInformationResponse(dict):
    def __init__(
        __self__,
        *,
        availability_stage: _builtins.str,
        disabled_reason: _builtins.str,
        disabled_reason_message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStage")
    def availability_stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disabledReasonMessage")
    def disabled_reason_message(self) -> _builtins.str: ...

@pulumi.output_type
class BillingMeterDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        frequency: _builtins.str,
        meter_details: Any,
        metering_type: _builtins.str,
        name: _builtins.str,
        term_type_details: outputs.TermTypeDetailsResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="meterDetails")
    def meter_details(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="meteringType")
    def metering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="termTypeDetails")
    def term_type_details(self) -> outputs.TermTypeDetailsResponse: ...

@pulumi.output_type
class CategoryInformationResponse(dict):
    def __init__(
        __self__,
        *,
        category_display_name: Optional[_builtins.str] = ...,
        category_name: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        links: Optional[Sequence[outputs.LinkResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="categoryDisplayName")
    def category_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="categoryName")
    def category_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[Sequence[outputs.LinkResponse]]: ...

@pulumi.output_type
class ChildConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        availability_information: outputs.AvailabilityInformationResponse,
        child_configuration_type: _builtins.str,
        child_configuration_types: Sequence[_builtins.str],
        cost_information: outputs.CostInformationResponse,
        description: outputs.DescriptionResponse,
        dimensions: outputs.DimensionsResponse,
        display_name: _builtins.str,
        filterable_properties: Sequence[outputs.FilterablePropertyResponse],
        fulfilled_by: _builtins.str,
        grouped_child_configurations: Sequence[
            outputs.GroupedChildConfigurationsResponse
        ],
        hierarchy_information: outputs.HierarchyInformationResponse,
        image_information: Sequence[outputs.ImageInformationResponse],
        is_part_of_base_configuration: _builtins.bool,
        maximum_quantity: _builtins.int,
        minimum_quantity: _builtins.int,
        provisioning_support: _builtins.str,
        specifications: Sequence[outputs.SpecificationResponse],
        supported_term_commitment_durations: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> outputs.AvailabilityInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="childConfigurationType")
    def child_configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="childConfigurationTypes")
    def child_configuration_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> outputs.CostInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> outputs.DescriptionResponse: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> outputs.DimensionsResponse: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence[outputs.FilterablePropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fulfilledBy")
    def fulfilled_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupedChildConfigurations")
    def grouped_child_configurations(
        self,
    ) -> Sequence[outputs.GroupedChildConfigurationsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence[outputs.ImageInformationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isPartOfBaseConfiguration")
    def is_part_of_base_configuration(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maximumQuantity")
    def maximum_quantity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minimumQuantity")
    def minimum_quantity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisioningSupport")
    def provisioning_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def specifications(self) -> Sequence[outputs.SpecificationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="supportedTermCommitmentDurations")
    def supported_term_commitment_durations(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ConfigurationDeviceDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_details: Sequence[outputs.DeviceDetailsResponse],
        hierarchy_information: outputs.HierarchyInformationResponse,
        identification_type: _builtins.str,
        quantity: _builtins.int,
        term_commitment_information: outputs.TermCommitmentInformationResponse,
        display_info: Optional[outputs.DisplayInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceDetails")
    def device_details(self) -> Sequence[outputs.DeviceDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="identificationType")
    def identification_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="termCommitmentInformation")
    def term_commitment_information(
        self,
    ) -> outputs.TermCommitmentInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="displayInfo")
    def display_info(self) -> Optional[outputs.DisplayInfoResponse]: ...

@pulumi.output_type
class ConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        availability_information: outputs.AvailabilityInformationResponse,
        child_configuration_types: Sequence[_builtins.str],
        cost_information: outputs.CostInformationResponse,
        description: outputs.DescriptionResponse,
        dimensions: outputs.DimensionsResponse,
        display_name: _builtins.str,
        filterable_properties: Sequence[outputs.FilterablePropertyResponse],
        fulfilled_by: _builtins.str,
        grouped_child_configurations: Sequence[
            outputs.GroupedChildConfigurationsResponse
        ],
        hierarchy_information: outputs.HierarchyInformationResponse,
        image_information: Sequence[outputs.ImageInformationResponse],
        provisioning_support: _builtins.str,
        specifications: Sequence[outputs.SpecificationResponse],
        supported_term_commitment_durations: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> outputs.AvailabilityInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="childConfigurationTypes")
    def child_configuration_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> outputs.CostInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> outputs.DescriptionResponse: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> outputs.DimensionsResponse: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence[outputs.FilterablePropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fulfilledBy")
    def fulfilled_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupedChildConfigurations")
    def grouped_child_configurations(
        self,
    ) -> Sequence[outputs.GroupedChildConfigurationsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence[outputs.ImageInformationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningSupport")
    def provisioning_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def specifications(self) -> Sequence[outputs.SpecificationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="supportedTermCommitmentDurations")
    def supported_term_commitment_durations(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ContactDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        contact_name: Optional[_builtins.str] = ...,
        email_list: Optional[Sequence[_builtins.str]] = ...,
        mobile: Optional[_builtins.str] = ...,
        phone: Optional[_builtins.str] = ...,
        phone_extension: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailList")
    def email_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def mobile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneExtension")
    def phone_extension(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CostInformationResponse(dict):
    def __init__(
        __self__,
        *,
        billing_info_url: _builtins.str,
        billing_meter_details: Sequence[outputs.BillingMeterDetailsResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingInfoUrl")
    def billing_info_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingMeterDetails")
    def billing_meter_details(
        self,
    ) -> Sequence[outputs.BillingMeterDetailsResponse]: ...

@pulumi.output_type
class DescriptionResponse(dict):
    def __init__(
        __self__,
        *,
        attributes: Sequence[_builtins.str],
        description_type: _builtins.str,
        keywords: Sequence[_builtins.str],
        links: Sequence[outputs.LinkResponse],
        long_description: _builtins.str,
        short_description: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="descriptionType")
    def description_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def keywords(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> Sequence[outputs.LinkResponse]: ...
    @_builtins.property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> _builtins.str: ...

@pulumi.output_type
class DeviceDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_serial_number: _builtins.str,
        management_resource_id: _builtins.str,
        management_resource_tenant_id: _builtins.str,
        provisioning_details: outputs.ProvisioningDetailsResponse,
        provisioning_support: _builtins.str,
        serial_number: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displaySerialNumber")
    def display_serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementResourceId")
    def management_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementResourceTenantId")
    def management_resource_tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningDetails")
    def provisioning_details(self) -> outputs.ProvisioningDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningSupport")
    def provisioning_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...

@pulumi.output_type
class DevicePresenceVerificationDetailsResponse(dict):
    def __init__(
        __self__, *, message: _builtins.str, status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class DimensionsResponse(dict):
    def __init__(
        __self__,
        *,
        depth: _builtins.float,
        height: _builtins.float,
        length: _builtins.float,
        length_height_unit: _builtins.str,
        weight: _builtins.float,
        weight_unit: _builtins.str,
        width: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def depth(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def height(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="lengthHeightUnit")
    def length_height_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="weightUnit")
    def weight_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def width(self) -> _builtins.float: ...

@pulumi.output_type
class DisplayInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_display_name: _builtins.str,
        product_family_display_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationDisplayName")
    def configuration_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productFamilyDisplayName")
    def product_family_display_name(self) -> _builtins.str: ...

@pulumi.output_type
class EncryptionPreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, double_encryption_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="doubleEncryptionStatus")
    def double_encryption_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDetailResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.ErrorAdditionalInfoResponse],
        code: _builtins.str,
        details: Sequence[outputs.ErrorDetailResponse],
        message: _builtins.str,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class FilterablePropertyResponse(dict):
    def __init__(
        __self__, *, supported_values: Sequence[_builtins.str], type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportedValues")
    def supported_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ForwardShippingDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        carrier_display_name: _builtins.str,
        carrier_name: _builtins.str,
        tracking_id: _builtins.str,
        tracking_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierDisplayName")
    def carrier_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackingUrl")
    def tracking_url(self) -> _builtins.str: ...

@pulumi.output_type
class GroupedChildConfigurationsResponse(dict):
    def __init__(
        __self__,
        *,
        category_information: outputs.CategoryInformationResponse,
        child_configurations: Sequence[outputs.ChildConfigurationResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="categoryInformation")
    def category_information(self) -> outputs.CategoryInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="childConfigurations")
    def child_configurations(self) -> Sequence[outputs.ChildConfigurationResponse]: ...

@pulumi.output_type
class HierarchyInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_id_display_name: Optional[_builtins.str] = ...,
        configuration_name: Optional[_builtins.str] = ...,
        product_family_name: Optional[_builtins.str] = ...,
        product_line_name: Optional[_builtins.str] = ...,
        product_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationIdDisplayName")
    def configuration_id_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productLineName")
    def product_line_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageInformationResponse(dict):
    def __init__(
        __self__, *, image_type: _builtins.str, image_url: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> _builtins.str: ...

@pulumi.output_type
class LinkResponse(dict):
    def __init__(
        __self__, *, link_type: _builtins.str, link_url: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkUrl")
    def link_url(self) -> _builtins.str: ...

@pulumi.output_type
class ManagementResourcePreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, preferred_management_resource_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredManagementResourceId")
    def preferred_management_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationPreferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, send_notification: _builtins.bool, stage_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sendNotification")
    def send_notification(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> _builtins.str: ...

@pulumi.output_type
class OrderItemDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cancellation_reason: _builtins.str,
        cancellation_status: _builtins.str,
        current_stage: outputs.StageDetailsResponse,
        deletion_status: _builtins.str,
        error: outputs.ErrorDetailResponse,
        forward_shipping_details: outputs.ForwardShippingDetailsResponse,
        management_rp_details_list: Sequence[outputs.ResourceProviderDetailsResponse],
        order_item_stage_history: Sequence[outputs.StageDetailsResponse],
        order_item_type: _builtins.str,
        product_details: outputs.ProductDetailsResponse,
        return_reason: _builtins.str,
        return_status: _builtins.str,
        reverse_shipping_details: outputs.ReverseShippingDetailsResponse,
        notification_email_list: Optional[Sequence[_builtins.str]] = ...,
        order_item_mode: Optional[_builtins.str] = ...,
        preferences: Optional[outputs.PreferencesResponse] = ...,
        site_details: Optional[outputs.SiteDetailsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cancellationReason")
    def cancellation_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cancellationStatus")
    def cancellation_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="currentStage")
    def current_stage(self) -> outputs.StageDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="deletionStatus")
    def deletion_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse: ...
    @_builtins.property
    @pulumi.getter(name="forwardShippingDetails")
    def forward_shipping_details(self) -> outputs.ForwardShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="managementRpDetailsList")
    def management_rp_details_list(
        self,
    ) -> Sequence[outputs.ResourceProviderDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="orderItemStageHistory")
    def order_item_stage_history(self) -> Sequence[outputs.StageDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="orderItemType")
    def order_item_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productDetails")
    def product_details(self) -> outputs.ProductDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="returnReason")
    def return_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="returnStatus")
    def return_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reverseShippingDetails")
    def reverse_shipping_details(self) -> outputs.ReverseShippingDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="notificationEmailList")
    def notification_email_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="orderItemMode")
    def order_item_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[outputs.PreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="siteDetails")
    def site_details(self) -> Optional[outputs.SiteDetailsResponse]: ...

@pulumi.output_type
class Pav2MeterDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        billing_type: _builtins.str,
        charging_type: _builtins.str,
        meter_guid: _builtins.str,
        multiplier: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="chargingType")
    def charging_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="meterGuid")
    def meter_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def multiplier(self) -> _builtins.float: ...

@pulumi.output_type
class PreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_preferences: Optional[outputs.EncryptionPreferencesResponse] = ...,
        management_resource_preferences: Optional[
            outputs.ManagementResourcePreferencesResponse
        ] = ...,
        notification_preferences: Optional[
            Sequence[outputs.NotificationPreferenceResponse]
        ] = ...,
        term_commitment_preferences: Optional[
            outputs.TermCommitmentPreferencesResponse
        ] = ...,
        transport_preferences: Optional[outputs.TransportPreferencesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionPreferences")
    def encryption_preferences(
        self,
    ) -> Optional[outputs.EncryptionPreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managementResourcePreferences")
    def management_resource_preferences(
        self,
    ) -> Optional[outputs.ManagementResourcePreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="notificationPreferences")
    def notification_preferences(
        self,
    ) -> Optional[Sequence[outputs.NotificationPreferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="termCommitmentPreferences")
    def term_commitment_preferences(
        self,
    ) -> Optional[outputs.TermCommitmentPreferencesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="transportPreferences")
    def transport_preferences(
        self,
    ) -> Optional[outputs.TransportPreferencesResponse]: ...

@pulumi.output_type
class ProductDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        child_configuration_device_details: Sequence[
            outputs.ConfigurationDeviceDetailsResponse
        ],
        hierarchy_information: outputs.HierarchyInformationResponse,
        identification_type: _builtins.str,
        parent_device_details: outputs.DeviceDetailsResponse,
        product_double_encryption_status: _builtins.str,
        term_commitment_information: outputs.TermCommitmentInformationResponse,
        display_info: Optional[outputs.DisplayInfoResponse] = ...,
        opt_in_additional_configurations: Optional[
            Sequence[outputs.AdditionalConfigurationResponse]
        ] = ...,
        parent_provisioning_details: Optional[
            outputs.ProvisioningDetailsResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="childConfigurationDeviceDetails")
    def child_configuration_device_details(
        self,
    ) -> Sequence[outputs.ConfigurationDeviceDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="identificationType")
    def identification_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parentDeviceDetails")
    def parent_device_details(self) -> outputs.DeviceDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="productDoubleEncryptionStatus")
    def product_double_encryption_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="termCommitmentInformation")
    def term_commitment_information(
        self,
    ) -> outputs.TermCommitmentInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="displayInfo")
    def display_info(self) -> Optional[outputs.DisplayInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="optInAdditionalConfigurations")
    def opt_in_additional_configurations(
        self,
    ) -> Optional[Sequence[outputs.AdditionalConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="parentProvisioningDetails")
    def parent_provisioning_details(
        self,
    ) -> Optional[outputs.ProvisioningDetailsResponse]: ...

@pulumi.output_type
class ProductFamilyResponse(dict):
    def __init__(
        __self__,
        *,
        availability_information: outputs.AvailabilityInformationResponse,
        cost_information: outputs.CostInformationResponse,
        description: outputs.DescriptionResponse,
        display_name: _builtins.str,
        filterable_properties: Sequence[outputs.FilterablePropertyResponse],
        fulfilled_by: _builtins.str,
        hierarchy_information: outputs.HierarchyInformationResponse,
        image_information: Sequence[outputs.ImageInformationResponse],
        product_lines: Sequence[outputs.ProductLineResponse],
        resource_provider_details: Optional[
            Sequence[outputs.ResourceProviderDetailsResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> outputs.AvailabilityInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> outputs.CostInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> outputs.DescriptionResponse: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence[outputs.FilterablePropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fulfilledBy")
    def fulfilled_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence[outputs.ImageInformationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="productLines")
    def product_lines(self) -> Sequence[outputs.ProductLineResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderDetails")
    def resource_provider_details(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderDetailsResponse]]: ...

@pulumi.output_type
class ProductLineResponse(dict):
    def __init__(
        __self__,
        *,
        availability_information: outputs.AvailabilityInformationResponse,
        cost_information: outputs.CostInformationResponse,
        description: outputs.DescriptionResponse,
        display_name: _builtins.str,
        filterable_properties: Sequence[outputs.FilterablePropertyResponse],
        fulfilled_by: _builtins.str,
        hierarchy_information: outputs.HierarchyInformationResponse,
        image_information: Sequence[outputs.ImageInformationResponse],
        products: Sequence[outputs.ProductResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> outputs.AvailabilityInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> outputs.CostInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> outputs.DescriptionResponse: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence[outputs.FilterablePropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fulfilledBy")
    def fulfilled_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence[outputs.ImageInformationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def products(self) -> Sequence[outputs.ProductResponse]: ...

@pulumi.output_type
class ProductResponse(dict):
    def __init__(
        __self__,
        *,
        availability_information: outputs.AvailabilityInformationResponse,
        configurations: Sequence[outputs.ConfigurationResponse],
        cost_information: outputs.CostInformationResponse,
        description: outputs.DescriptionResponse,
        display_name: _builtins.str,
        filterable_properties: Sequence[outputs.FilterablePropertyResponse],
        fulfilled_by: _builtins.str,
        hierarchy_information: outputs.HierarchyInformationResponse,
        image_information: Sequence[outputs.ImageInformationResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> outputs.AvailabilityInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Sequence[outputs.ConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> outputs.CostInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> outputs.DescriptionResponse: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence[outputs.FilterablePropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fulfilledBy")
    def fulfilled_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> outputs.HierarchyInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence[outputs.ImageInformationResponse]: ...

@pulumi.output_type
class ProvisioningDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        unique_device_identifier: _builtins.str,
        auto_provisioning_status: Optional[_builtins.str] = ...,
        device_presence_verification: Optional[
            outputs.DevicePresenceVerificationDetailsResponse
        ] = ...,
        management_resource_arm_id: Optional[_builtins.str] = ...,
        provisioning_arm_id: Optional[_builtins.str] = ...,
        provisioning_end_point: Optional[_builtins.str] = ...,
        quantity: Optional[_builtins.int] = ...,
        ready_to_connect_arm_id: Optional[_builtins.str] = ...,
        serial_number: Optional[_builtins.str] = ...,
        vendor_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uniqueDeviceIdentifier")
    def unique_device_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisioningStatus")
    def auto_provisioning_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="devicePresenceVerification")
    def device_presence_verification(
        self,
    ) -> Optional[outputs.DevicePresenceVerificationDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managementResourceArmId")
    def management_resource_arm_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningArmId")
    def provisioning_arm_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningEndPoint")
    def provisioning_end_point(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="readyToConnectArmId")
    def ready_to_connect_arm_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PurchaseMeterDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        billing_type: _builtins.str,
        charging_type: _builtins.str,
        multiplier: _builtins.float,
        product_id: _builtins.str,
        sku_id: _builtins.str,
        term_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="chargingType")
    def charging_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def multiplier(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="termId")
    def term_id(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ResourceProviderDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_provider_namespace: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderNamespace")
    def resource_provider_namespace(self) -> _builtins.str: ...

@pulumi.output_type
class ReverseShippingDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        carrier_display_name: _builtins.str,
        carrier_name: _builtins.str,
        sas_key_for_label: _builtins.str,
        tracking_id: _builtins.str,
        tracking_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierDisplayName")
    def carrier_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sasKeyForLabel")
    def sas_key_for_label(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackingUrl")
    def tracking_url(self) -> _builtins.str: ...

@pulumi.output_type
class ShippingAddressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        country: _builtins.str,
        address_type: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        company_name: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        state_or_province: Optional[_builtins.str] = ...,
        street_address1: Optional[_builtins.str] = ...,
        street_address2: Optional[_builtins.str] = ...,
        street_address3: Optional[_builtins.str] = ...,
        zip_extended_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressType")
    def address_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress2")
    def street_address2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress3")
    def street_address3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipExtendedCode")
    def zip_extended_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SiteDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, site_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str: ...

@pulumi.output_type
class SpecificationResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class StageDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: _builtins.str,
        stage_name: _builtins.str,
        stage_status: _builtins.str,
        start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stageStatus")
    def stage_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

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

@pulumi.output_type
class TermCommitmentInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pending_days_for_term: Optional[_builtins.int] = ...,
        term_commitment_type: _builtins.str,
        term_commitment_type_duration: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pendingDaysForTerm")
    def pending_days_for_term(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="termCommitmentType")
    def term_commitment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="termCommitmentTypeDuration")
    def term_commitment_type_duration(self) -> _builtins.str: ...

@pulumi.output_type
class TermCommitmentPreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        preferred_term_commitment_type: _builtins.str,
        preferred_term_commitment_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredTermCommitmentType")
    def preferred_term_commitment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredTermCommitmentDuration")
    def preferred_term_commitment_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TermTypeDetailsResponse(dict):
    def __init__(
        __self__, *, term_type: _builtins.str, term_type_duration: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="termType")
    def term_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="termTypeDuration")
    def term_type_duration(self) -> _builtins.str: ...

@pulumi.output_type
class TransportPreferencesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, preferred_shipment_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredShipmentType")
    def preferred_shipment_type(self) -> _builtins.str: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

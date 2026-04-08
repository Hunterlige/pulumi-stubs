import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssociatedTenantPropertiesArgs",
    "AssociatedTenantPropertiesArgsDict",
    "AzurePlanArgs",
    "AzurePlanArgsDict",
    "BillingProfilePropertiesBillToArgs",
    "BillingProfilePropertiesBillToArgsDict",
    "BillingProfilePropertiesCurrentPaymentTermArgs",
    "BillingProfilePropertiesCurrentPaymentTermArgsDict",
    ...,
    ...,
    "BillingProfilePropertiesShipToArgs",
    "BillingProfilePropertiesShipToArgsDict",
    "BillingProfilePropertiesSoldToArgs",
    "BillingProfilePropertiesSoldToArgsDict",
    "BillingProfilePropertiesArgs",
    "BillingProfilePropertiesArgsDict",
    "BillingRoleAssignmentPropertiesArgs",
    "BillingRoleAssignmentPropertiesArgsDict",
    "InvoiceSectionPropertiesArgs",
    "InvoiceSectionPropertiesArgsDict",
]

class AssociatedTenantPropertiesArgsDict(TypedDict):
    billing_management_state: NotRequired[
        pulumi.Input[Union[_builtins.str, BillingManagementTenantState]]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_management_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ProvisioningTenantState]]
    ]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AssociatedTenantPropertiesArgs:
    def __init__(
        __self__,
        *,
        billing_management_state: Optional[
            pulumi.Input[Union[_builtins.str, BillingManagementTenantState]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_management_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningTenantState]]
        ] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingManagementState")
    def billing_management_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BillingManagementTenantState]]]: ...
    @billing_management_state.setter
    def billing_management_state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, BillingManagementTenantState]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningManagementState")
    def provisioning_management_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningTenantState]]]: ...
    @provisioning_management_state.setter
    def provisioning_management_state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningTenantState]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzurePlanArgsDict(TypedDict):
    product_id: NotRequired[pulumi.Input[_builtins.str]]
    sku_description: NotRequired[pulumi.Input[_builtins.str]]
    sku_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzurePlanArgs:
    def __init__(
        __self__,
        *,
        product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku_description: Optional[pulumi.Input[_builtins.str]] = ...,
        sku_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skuDescription")
    def sku_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_description.setter
    def sku_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_id.setter
    def sku_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BillingProfilePropertiesBillToArgsDict(TypedDict):
    address_line1: pulumi.Input[_builtins.str]
    country: pulumi.Input[_builtins.str]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    address_line3: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    company_name: NotRequired[pulumi.Input[_builtins.str]]
    district: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    is_valid_address: NotRequired[pulumi.Input[_builtins.bool]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    middle_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingProfilePropertiesBillToArgs:
    def __init__(
        __self__,
        *,
        address_line1: pulumi.Input[_builtins.str],
        country: pulumi.Input[_builtins.str],
        address_line2: Optional[pulumi.Input[_builtins.str]] = ...,
        address_line3: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        company_name: Optional[pulumi.Input[_builtins.str]] = ...,
        district: Optional[pulumi.Input[_builtins.str]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_valid_address: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> pulumi.Input[_builtins.str]: ...
    @address_line1.setter
    def address_line1(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> pulumi.Input[_builtins.str]: ...
    @country.setter
    def country(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line3.setter
    def address_line3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @district.setter
    def district(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isValidAddress")
    def is_valid_address(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_valid_address.setter
    def is_valid_address(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @middle_name.setter
    def middle_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BillingProfilePropertiesCurrentPaymentTermArgsDict(TypedDict):
    end_date: NotRequired[pulumi.Input[_builtins.str]]
    start_date: NotRequired[pulumi.Input[_builtins.str]]
    term: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingProfilePropertiesCurrentPaymentTermArgs:
    def __init__(
        __self__,
        *,
        end_date: Optional[pulumi.Input[_builtins.str]] = ...,
        start_date: Optional[pulumi.Input[_builtins.str]] = ...,
        term: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def term(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @term.setter
    def term(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BillingProfilePropertiesIndirectRelationshipInfoArgsDict(TypedDict):
    billing_account_name: NotRequired[pulumi.Input[_builtins.str]]
    billing_profile_name: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingProfilePropertiesIndirectRelationshipInfoArgs:
    def __init__(
        __self__,
        *,
        billing_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        billing_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountName")
    def billing_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_account_name.setter
    def billing_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="billingProfileName")
    def billing_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_profile_name.setter
    def billing_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BillingProfilePropertiesShipToArgsDict(TypedDict):
    address_line1: pulumi.Input[_builtins.str]
    country: pulumi.Input[_builtins.str]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    address_line3: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    company_name: NotRequired[pulumi.Input[_builtins.str]]
    district: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    is_valid_address: NotRequired[pulumi.Input[_builtins.bool]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    middle_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingProfilePropertiesShipToArgs:
    def __init__(
        __self__,
        *,
        address_line1: pulumi.Input[_builtins.str],
        country: pulumi.Input[_builtins.str],
        address_line2: Optional[pulumi.Input[_builtins.str]] = ...,
        address_line3: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        company_name: Optional[pulumi.Input[_builtins.str]] = ...,
        district: Optional[pulumi.Input[_builtins.str]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_valid_address: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> pulumi.Input[_builtins.str]: ...
    @address_line1.setter
    def address_line1(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> pulumi.Input[_builtins.str]: ...
    @country.setter
    def country(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line3.setter
    def address_line3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @district.setter
    def district(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isValidAddress")
    def is_valid_address(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_valid_address.setter
    def is_valid_address(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @middle_name.setter
    def middle_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BillingProfilePropertiesSoldToArgsDict(TypedDict):
    address_line1: pulumi.Input[_builtins.str]
    country: pulumi.Input[_builtins.str]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    address_line3: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    company_name: NotRequired[pulumi.Input[_builtins.str]]
    district: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    is_valid_address: NotRequired[pulumi.Input[_builtins.bool]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    middle_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingProfilePropertiesSoldToArgs:
    def __init__(
        __self__,
        *,
        address_line1: pulumi.Input[_builtins.str],
        country: pulumi.Input[_builtins.str],
        address_line2: Optional[pulumi.Input[_builtins.str]] = ...,
        address_line3: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        company_name: Optional[pulumi.Input[_builtins.str]] = ...,
        district: Optional[pulumi.Input[_builtins.str]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_valid_address: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> pulumi.Input[_builtins.str]: ...
    @address_line1.setter
    def address_line1(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> pulumi.Input[_builtins.str]: ...
    @country.setter
    def country(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line3.setter
    def address_line3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @district.setter
    def district(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isValidAddress")
    def is_valid_address(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_valid_address.setter
    def is_valid_address(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @middle_name.setter
    def middle_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BillingProfilePropertiesArgsDict(TypedDict):
    bill_to: NotRequired[pulumi.Input[BillingProfilePropertiesBillToArgsDict]]
    current_payment_term: NotRequired[
        pulumi.Input[BillingProfilePropertiesCurrentPaymentTermArgsDict]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    enabled_azure_plans: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AzurePlanArgsDict]]]
    ]
    indirect_relationship_info: NotRequired[
        pulumi.Input[BillingProfilePropertiesIndirectRelationshipInfoArgsDict]
    ]
    invoice_email_opt_in: NotRequired[pulumi.Input[_builtins.bool]]
    invoice_recipients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    po_number: NotRequired[pulumi.Input[_builtins.str]]
    ship_to: NotRequired[pulumi.Input[BillingProfilePropertiesShipToArgsDict]]
    sold_to: NotRequired[pulumi.Input[BillingProfilePropertiesSoldToArgsDict]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BillingProfilePropertiesArgs:
    def __init__(
        __self__,
        *,
        bill_to: Optional[pulumi.Input[BillingProfilePropertiesBillToArgs]] = ...,
        current_payment_term: Optional[
            pulumi.Input[BillingProfilePropertiesCurrentPaymentTermArgs]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_azure_plans: Optional[
            pulumi.Input[Sequence[pulumi.Input[AzurePlanArgs]]]
        ] = ...,
        indirect_relationship_info: Optional[
            pulumi.Input[BillingProfilePropertiesIndirectRelationshipInfoArgs]
        ] = ...,
        invoice_email_opt_in: Optional[pulumi.Input[_builtins.bool]] = ...,
        invoice_recipients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        po_number: Optional[pulumi.Input[_builtins.str]] = ...,
        ship_to: Optional[pulumi.Input[BillingProfilePropertiesShipToArgs]] = ...,
        sold_to: Optional[pulumi.Input[BillingProfilePropertiesSoldToArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billTo")
    def bill_to(self) -> Optional[pulumi.Input[BillingProfilePropertiesBillToArgs]]: ...
    @bill_to.setter
    def bill_to(
        self, value: Optional[pulumi.Input[BillingProfilePropertiesBillToArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="currentPaymentTerm")
    def current_payment_term(
        self,
    ) -> Optional[pulumi.Input[BillingProfilePropertiesCurrentPaymentTermArgs]]: ...
    @current_payment_term.setter
    def current_payment_term(
        self,
        value: Optional[pulumi.Input[BillingProfilePropertiesCurrentPaymentTermArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enabledAzurePlans")
    def enabled_azure_plans(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzurePlanArgs]]]]: ...
    @enabled_azure_plans.setter
    def enabled_azure_plans(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzurePlanArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="indirectRelationshipInfo")
    def indirect_relationship_info(
        self,
    ) -> Optional[
        pulumi.Input[BillingProfilePropertiesIndirectRelationshipInfoArgs]
    ]: ...
    @indirect_relationship_info.setter
    def indirect_relationship_info(
        self,
        value: Optional[
            pulumi.Input[BillingProfilePropertiesIndirectRelationshipInfoArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="invoiceEmailOptIn")
    def invoice_email_opt_in(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invoice_email_opt_in.setter
    def invoice_email_opt_in(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="invoiceRecipients")
    def invoice_recipients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @invoice_recipients.setter
    def invoice_recipients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="poNumber")
    def po_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @po_number.setter
    def po_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shipTo")
    def ship_to(self) -> Optional[pulumi.Input[BillingProfilePropertiesShipToArgs]]: ...
    @ship_to.setter
    def ship_to(
        self, value: Optional[pulumi.Input[BillingProfilePropertiesShipToArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="soldTo")
    def sold_to(self) -> Optional[pulumi.Input[BillingProfilePropertiesSoldToArgs]]: ...
    @sold_to.setter
    def sold_to(
        self, value: Optional[pulumi.Input[BillingProfilePropertiesSoldToArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class BillingRoleAssignmentPropertiesArgsDict(TypedDict):
    role_definition_id: pulumi.Input[_builtins.str]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_puid: NotRequired[pulumi.Input[_builtins.str]]
    principal_tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    user_authentication_type: NotRequired[pulumi.Input[_builtins.str]]
    user_email_address: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingRoleAssignmentPropertiesArgs:
    def __init__(
        __self__,
        *,
        role_definition_id: pulumi.Input[_builtins.str],
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_puid: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        user_authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[_builtins.str]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalPuid")
    def principal_puid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_puid.setter
    def principal_puid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalTenantId")
    def principal_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_tenant_id.setter
    def principal_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userAuthenticationType")
    def user_authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_authentication_type.setter
    def user_authentication_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userEmailAddress")
    def user_email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_email_address.setter
    def user_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InvoiceSectionPropertiesArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    reason_code: NotRequired[
        pulumi.Input[Union[_builtins.str, InvoiceSectionStateReasonCode]]
    ]
    state: NotRequired[pulumi.Input[Union[_builtins.str, InvoiceSectionState]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_cloud: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InvoiceSectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        reason_code: Optional[
            pulumi.Input[Union[_builtins.str, InvoiceSectionStateReasonCode]]
        ] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, InvoiceSectionState]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_cloud: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reasonCode")
    def reason_code(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, InvoiceSectionStateReasonCode]]
    ]: ...
    @reason_code.setter
    def reason_code(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, InvoiceSectionStateReasonCode]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InvoiceSectionState]]]: ...
    @state.setter
    def state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InvoiceSectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetCloud")
    def target_cloud(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_cloud.setter
    def target_cloud(self, value: Optional[pulumi.Input[_builtins.str]]): ...

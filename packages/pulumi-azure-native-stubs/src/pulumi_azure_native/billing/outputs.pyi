import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssociatedTenantPropertiesResponse",
    "AzurePlanResponse",
    "BillingProfilePropertiesResponse",
    "BillingProfilePropertiesResponseBillTo",
    "BillingProfilePropertiesResponseCurrentPaymentTerm",
    ...,
    "BillingProfilePropertiesResponseShipTo",
    "BillingProfilePropertiesResponseSoldTo",
    "BillingRoleAssignmentPropertiesResponse",
    "InvoiceSectionPropertiesResponse",
    "InvoiceSectionWithCreateSubPermissionResponse",
    "PaymentTermResponse",
    "SpendingLimitDetailsResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class AssociatedTenantPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_billing_request_id: _builtins.str,
        provisioning_state: _builtins.str,
        billing_management_state: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        provisioning_management_state: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningBillingRequestId")
    def provisioning_billing_request_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingManagementState")
    def billing_management_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningManagementState")
    def provisioning_management_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzurePlanResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        product_id: Optional[_builtins.str] = ...,
        sku_description: Optional[_builtins.str] = ...,
        sku_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skuDescription")
    def sku_description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BillingProfilePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        billing_relationship_type: _builtins.str,
        currency: _builtins.str,
        has_read_access: _builtins.bool,
        invoice_day: _builtins.int,
        other_payment_terms: Sequence[outputs.PaymentTermResponse],
        provisioning_state: _builtins.str,
        spending_limit: _builtins.str,
        spending_limit_details: Sequence[outputs.SpendingLimitDetailsResponse],
        status: _builtins.str,
        status_reason_code: _builtins.str,
        system_id: _builtins.str,
        target_clouds: Sequence[_builtins.str],
        bill_to: Optional[outputs.BillingProfilePropertiesResponseBillTo] = ...,
        current_payment_term: Optional[
            outputs.BillingProfilePropertiesResponseCurrentPaymentTerm
        ] = ...,
        display_name: Optional[_builtins.str] = ...,
        enabled_azure_plans: Optional[Sequence[outputs.AzurePlanResponse]] = ...,
        indirect_relationship_info: Optional[
            outputs.BillingProfilePropertiesResponseIndirectRelationshipInfo
        ] = ...,
        invoice_email_opt_in: Optional[_builtins.bool] = ...,
        invoice_recipients: Optional[Sequence[_builtins.str]] = ...,
        po_number: Optional[_builtins.str] = ...,
        ship_to: Optional[outputs.BillingProfilePropertiesResponseShipTo] = ...,
        sold_to: Optional[outputs.BillingProfilePropertiesResponseSoldTo] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingRelationshipType")
    def billing_relationship_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def currency(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hasReadAccess")
    def has_read_access(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="invoiceDay")
    def invoice_day(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="otherPaymentTerms")
    def other_payment_terms(self) -> Sequence[outputs.PaymentTermResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="spendingLimit")
    def spending_limit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="spendingLimitDetails")
    def spending_limit_details(
        self,
    ) -> Sequence[outputs.SpendingLimitDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReasonCode")
    def status_reason_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetClouds")
    def target_clouds(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="billTo")
    def bill_to(self) -> Optional[outputs.BillingProfilePropertiesResponseBillTo]: ...
    @_builtins.property
    @pulumi.getter(name="currentPaymentTerm")
    def current_payment_term(
        self,
    ) -> Optional[outputs.BillingProfilePropertiesResponseCurrentPaymentTerm]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledAzurePlans")
    def enabled_azure_plans(self) -> Optional[Sequence[outputs.AzurePlanResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="indirectRelationshipInfo")
    def indirect_relationship_info(
        self,
    ) -> Optional[outputs.BillingProfilePropertiesResponseIndirectRelationshipInfo]: ...
    @_builtins.property
    @pulumi.getter(name="invoiceEmailOptIn")
    def invoice_email_opt_in(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="invoiceRecipients")
    def invoice_recipients(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="poNumber")
    def po_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shipTo")
    def ship_to(self) -> Optional[outputs.BillingProfilePropertiesResponseShipTo]: ...
    @_builtins.property
    @pulumi.getter(name="soldTo")
    def sold_to(self) -> Optional[outputs.BillingProfilePropertiesResponseSoldTo]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class BillingProfilePropertiesResponseBillTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: _builtins.str,
        country: _builtins.str,
        address_line2: Optional[_builtins.str] = ...,
        address_line3: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        company_name: Optional[_builtins.str] = ...,
        district: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        is_valid_address: Optional[_builtins.bool] = ...,
        last_name: Optional[_builtins.str] = ...,
        middle_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isValidAddress")
    def is_valid_address(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BillingProfilePropertiesResponseCurrentPaymentTerm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_default: _builtins.bool,
        end_date: Optional[_builtins.str] = ...,
        start_date: Optional[_builtins.str] = ...,
        term: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def term(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BillingProfilePropertiesResponseIndirectRelationshipInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        billing_account_name: Optional[_builtins.str] = ...,
        billing_profile_name: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountName")
    def billing_account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileName")
    def billing_profile_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BillingProfilePropertiesResponseShipTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: _builtins.str,
        country: _builtins.str,
        address_line2: Optional[_builtins.str] = ...,
        address_line3: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        company_name: Optional[_builtins.str] = ...,
        district: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        is_valid_address: Optional[_builtins.bool] = ...,
        last_name: Optional[_builtins.str] = ...,
        middle_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isValidAddress")
    def is_valid_address(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BillingProfilePropertiesResponseSoldTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: _builtins.str,
        country: _builtins.str,
        address_line2: Optional[_builtins.str] = ...,
        address_line3: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        company_name: Optional[_builtins.str] = ...,
        district: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        is_valid_address: Optional[_builtins.bool] = ...,
        last_name: Optional[_builtins.str] = ...,
        middle_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isValidAddress")
    def is_valid_address(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BillingRoleAssignmentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        billing_account_display_name: _builtins.str,
        billing_account_id: _builtins.str,
        billing_profile_display_name: _builtins.str,
        billing_profile_id: _builtins.str,
        billing_request_id: _builtins.str,
        created_by_principal_id: _builtins.str,
        created_by_principal_puid: _builtins.str,
        created_by_principal_tenant_id: _builtins.str,
        created_by_user_email_address: _builtins.str,
        created_on: _builtins.str,
        customer_display_name: _builtins.str,
        customer_id: _builtins.str,
        invoice_section_display_name: _builtins.str,
        invoice_section_id: _builtins.str,
        modified_by_principal_id: _builtins.str,
        modified_by_principal_puid: _builtins.str,
        modified_by_principal_tenant_id: _builtins.str,
        modified_by_user_email_address: _builtins.str,
        modified_on: _builtins.str,
        principal_display_name: _builtins.str,
        principal_tenant_name: _builtins.str,
        principal_type: _builtins.str,
        provisioning_state: _builtins.str,
        role_definition_id: _builtins.str,
        principal_id: Optional[_builtins.str] = ...,
        principal_puid: Optional[_builtins.str] = ...,
        principal_tenant_id: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
        user_authentication_type: Optional[_builtins.str] = ...,
        user_email_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountDisplayName")
    def billing_account_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileDisplayName")
    def billing_profile_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileId")
    def billing_profile_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingRequestId")
    def billing_request_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdByPrincipalId")
    def created_by_principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdByPrincipalPuid")
    def created_by_principal_puid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdByPrincipalTenantId")
    def created_by_principal_tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdByUserEmailAddress")
    def created_by_user_email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customerDisplayName")
    def customer_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invoiceSectionDisplayName")
    def invoice_section_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invoiceSectionId")
    def invoice_section_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modifiedByPrincipalId")
    def modified_by_principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modifiedByPrincipalPuid")
    def modified_by_principal_puid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modifiedByPrincipalTenantId")
    def modified_by_principal_tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modifiedByUserEmailAddress")
    def modified_by_user_email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalDisplayName")
    def principal_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalTenantName")
    def principal_tenant_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalPuid")
    def principal_puid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalTenantId")
    def principal_tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAuthenticationType")
    def user_authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userEmailAddress")
    def user_email_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InvoiceSectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        system_id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        reason_code: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        target_cloud: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reasonCode")
    def reason_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetCloud")
    def target_cloud(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InvoiceSectionWithCreateSubPermissionResponse(dict):
    def __init__(
        __self__,
        *,
        billing_profile_display_name: _builtins.str,
        billing_profile_id: _builtins.str,
        billing_profile_spending_limit: _builtins.str,
        billing_profile_status: _builtins.str,
        billing_profile_status_reason_code: _builtins.str,
        billing_profile_system_id: _builtins.str,
        enabled_azure_plans: Sequence[outputs.AzurePlanResponse],
        invoice_section_display_name: _builtins.str,
        invoice_section_id: _builtins.str,
        invoice_section_system_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileDisplayName")
    def billing_profile_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileId")
    def billing_profile_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileSpendingLimit")
    def billing_profile_spending_limit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileStatus")
    def billing_profile_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileStatusReasonCode")
    def billing_profile_status_reason_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileSystemId")
    def billing_profile_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledAzurePlans")
    def enabled_azure_plans(self) -> Sequence[outputs.AzurePlanResponse]: ...
    @_builtins.property
    @pulumi.getter(name="invoiceSectionDisplayName")
    def invoice_section_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invoiceSectionId")
    def invoice_section_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invoiceSectionSystemId")
    def invoice_section_system_id(self) -> _builtins.str: ...

@pulumi.output_type
class PaymentTermResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_default: _builtins.bool,
        end_date: Optional[_builtins.str] = ...,
        start_date: Optional[_builtins.str] = ...,
        term: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def term(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpendingLimitDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amount: Optional[_builtins.float] = ...,
        currency: Optional[_builtins.str] = ...,
        end_date: Optional[_builtins.str] = ...,
        start_date: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amount(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

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

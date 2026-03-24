import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProfileArgs", "Profile"]

@pulumi.input_type
class ProfileArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        account_number: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_information: Optional[pulumi.Input[_builtins.str]] = ...,
        address: Optional[pulumi.Input[ProfileAddressArgs]] = ...,
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        billing_address: Optional[pulumi.Input[ProfileBillingAddressArgs]] = ...,
        birth_date: Optional[pulumi.Input[_builtins.str]] = ...,
        business_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        business_name: Optional[pulumi.Input[_builtins.str]] = ...,
        business_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gender_string: Optional[pulumi.Input[_builtins.str]] = ...,
        home_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mailing_address: Optional[pulumi.Input[ProfileMailingAddressArgs]] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mobile_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        party_type_string: Optional[pulumi.Input[_builtins.str]] = ...,
        personal_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shipping_address: Optional[pulumi.Input[ProfileShippingAddressArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountNumber")
    def account_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_number.setter
    def account_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="additionalInformation")
    def additional_information(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_information.setter
    def additional_information(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[ProfileAddressArgs]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[ProfileAddressArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @attributes.setter
    def attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingAddress")
    def billing_address(self) -> Optional[pulumi.Input[ProfileBillingAddressArgs]]: ...
    @billing_address.setter
    def billing_address(
        self, value: Optional[pulumi.Input[ProfileBillingAddressArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="birthDate")
    def birth_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @birth_date.setter
    def birth_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="businessEmailAddress")
    def business_email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @business_email_address.setter
    def business_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="businessName")
    def business_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @business_name.setter
    def business_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="businessPhoneNumber")
    def business_phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @business_phone_number.setter
    def business_phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="genderString")
    def gender_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gender_string.setter
    def gender_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="homePhoneNumber")
    def home_phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @home_phone_number.setter
    def home_phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mailingAddress")
    def mailing_address(self) -> Optional[pulumi.Input[ProfileMailingAddressArgs]]: ...
    @mailing_address.setter
    def mailing_address(
        self, value: Optional[pulumi.Input[ProfileMailingAddressArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @middle_name.setter
    def middle_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mobilePhoneNumber")
    def mobile_phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mobile_phone_number.setter
    def mobile_phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partyTypeString")
    def party_type_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @party_type_string.setter
    def party_type_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="personalEmailAddress")
    def personal_email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @personal_email_address.setter
    def personal_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(
        self,
    ) -> Optional[pulumi.Input[ProfileShippingAddressArgs]]: ...
    @shipping_address.setter
    def shipping_address(
        self, value: Optional[pulumi.Input[ProfileShippingAddressArgs]]
    ): ...

@pulumi.input_type
class _ProfileState:
    def __init__(
        __self__,
        *,
        account_number: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_information: Optional[pulumi.Input[_builtins.str]] = ...,
        address: Optional[pulumi.Input[ProfileAddressArgs]] = ...,
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        billing_address: Optional[pulumi.Input[ProfileBillingAddressArgs]] = ...,
        birth_date: Optional[pulumi.Input[_builtins.str]] = ...,
        business_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        business_name: Optional[pulumi.Input[_builtins.str]] = ...,
        business_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gender_string: Optional[pulumi.Input[_builtins.str]] = ...,
        home_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mailing_address: Optional[pulumi.Input[ProfileMailingAddressArgs]] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mobile_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        party_type_string: Optional[pulumi.Input[_builtins.str]] = ...,
        personal_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shipping_address: Optional[pulumi.Input[ProfileShippingAddressArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountNumber")
    def account_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_number.setter
    def account_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="additionalInformation")
    def additional_information(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_information.setter
    def additional_information(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[ProfileAddressArgs]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[ProfileAddressArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @attributes.setter
    def attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingAddress")
    def billing_address(self) -> Optional[pulumi.Input[ProfileBillingAddressArgs]]: ...
    @billing_address.setter
    def billing_address(
        self, value: Optional[pulumi.Input[ProfileBillingAddressArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="birthDate")
    def birth_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @birth_date.setter
    def birth_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="businessEmailAddress")
    def business_email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @business_email_address.setter
    def business_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="businessName")
    def business_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @business_name.setter
    def business_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="businessPhoneNumber")
    def business_phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @business_phone_number.setter
    def business_phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="genderString")
    def gender_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gender_string.setter
    def gender_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="homePhoneNumber")
    def home_phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @home_phone_number.setter
    def home_phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mailingAddress")
    def mailing_address(self) -> Optional[pulumi.Input[ProfileMailingAddressArgs]]: ...
    @mailing_address.setter
    def mailing_address(
        self, value: Optional[pulumi.Input[ProfileMailingAddressArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @middle_name.setter
    def middle_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mobilePhoneNumber")
    def mobile_phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mobile_phone_number.setter
    def mobile_phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partyTypeString")
    def party_type_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @party_type_string.setter
    def party_type_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="personalEmailAddress")
    def personal_email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @personal_email_address.setter
    def personal_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(
        self,
    ) -> Optional[pulumi.Input[ProfileShippingAddressArgs]]: ...
    @shipping_address.setter
    def shipping_address(
        self, value: Optional[pulumi.Input[ProfileShippingAddressArgs]]
    ): ...

@pulumi.type_token("aws:customerprofiles/profile:Profile")
class Profile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_number: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_information: Optional[pulumi.Input[_builtins.str]] = ...,
        address: Optional[
            pulumi.Input[Union[ProfileAddressArgs, ProfileAddressArgsDict]]
        ] = ...,
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        billing_address: Optional[
            pulumi.Input[
                Union[ProfileBillingAddressArgs, ProfileBillingAddressArgsDict]
            ]
        ] = ...,
        birth_date: Optional[pulumi.Input[_builtins.str]] = ...,
        business_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        business_name: Optional[pulumi.Input[_builtins.str]] = ...,
        business_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gender_string: Optional[pulumi.Input[_builtins.str]] = ...,
        home_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mailing_address: Optional[
            pulumi.Input[
                Union[ProfileMailingAddressArgs, ProfileMailingAddressArgsDict]
            ]
        ] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mobile_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        party_type_string: Optional[pulumi.Input[_builtins.str]] = ...,
        personal_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shipping_address: Optional[
            pulumi.Input[
                Union[ProfileShippingAddressArgs, ProfileShippingAddressArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_number: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_information: Optional[pulumi.Input[_builtins.str]] = ...,
        address: Optional[
            pulumi.Input[Union[ProfileAddressArgs, ProfileAddressArgsDict]]
        ] = ...,
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        billing_address: Optional[
            pulumi.Input[
                Union[ProfileBillingAddressArgs, ProfileBillingAddressArgsDict]
            ]
        ] = ...,
        birth_date: Optional[pulumi.Input[_builtins.str]] = ...,
        business_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        business_name: Optional[pulumi.Input[_builtins.str]] = ...,
        business_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gender_string: Optional[pulumi.Input[_builtins.str]] = ...,
        home_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mailing_address: Optional[
            pulumi.Input[
                Union[ProfileMailingAddressArgs, ProfileMailingAddressArgsDict]
            ]
        ] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mobile_phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        party_type_string: Optional[pulumi.Input[_builtins.str]] = ...,
        personal_email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        shipping_address: Optional[
            pulumi.Input[
                Union[ProfileShippingAddressArgs, ProfileShippingAddressArgsDict]
            ]
        ] = ...,
    ) -> Profile: ...
    @_builtins.property
    @pulumi.getter(name="accountNumber")
    def account_number(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="additionalInformation")
    def additional_information(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Output[Optional[outputs.ProfileAddress]]: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="billingAddress")
    def billing_address(
        self,
    ) -> pulumi.Output[Optional[outputs.ProfileBillingAddress]]: ...
    @_builtins.property
    @pulumi.getter(name="birthDate")
    def birth_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="businessEmailAddress")
    def business_email_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="businessName")
    def business_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="businessPhoneNumber")
    def business_phone_number(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="genderString")
    def gender_string(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="homePhoneNumber")
    def home_phone_number(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="mailingAddress")
    def mailing_address(
        self,
    ) -> pulumi.Output[Optional[outputs.ProfileMailingAddress]]: ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="mobilePhoneNumber")
    def mobile_phone_number(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="partyTypeString")
    def party_type_string(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="personalEmailAddress")
    def personal_email_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(
        self,
    ) -> pulumi.Output[Optional[outputs.ProfileShippingAddress]]: ...

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstancePropertiesArgs",
    "InstancePropertiesArgsDict",
    "LiftrBaseMarketplaceDetailsArgs",
    "LiftrBaseMarketplaceDetailsArgsDict",
    "LiftrBaseOfferDetailsArgs",
    "LiftrBaseOfferDetailsArgsDict",
    "LiftrBaseSingleSignOnPropertiesV2Args",
    "LiftrBaseSingleSignOnPropertiesV2ArgsDict",
    "LiftrBaseUserDetailsArgs",
    "LiftrBaseUserDetailsArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "PartnerPropertiesArgs",
    "PartnerPropertiesArgsDict",
]

class InstancePropertiesArgsDict(TypedDict):
    marketplace: pulumi.Input[LiftrBaseMarketplaceDetailsArgsDict]
    user: pulumi.Input[LiftrBaseUserDetailsArgsDict]
    partner_properties: NotRequired[pulumi.Input[PartnerPropertiesArgsDict]]
    single_sign_on_properties: NotRequired[
        pulumi.Input[LiftrBaseSingleSignOnPropertiesV2ArgsDict]
    ]

@pulumi.input_type
class InstancePropertiesArgs:
    def __init__(
        __self__,
        *,
        marketplace: pulumi.Input[LiftrBaseMarketplaceDetailsArgs],
        user: pulumi.Input[LiftrBaseUserDetailsArgs],
        partner_properties: Optional[pulumi.Input[PartnerPropertiesArgs]] = ...,
        single_sign_on_properties: Optional[
            pulumi.Input[LiftrBaseSingleSignOnPropertiesV2Args]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def marketplace(self) -> pulumi.Input[LiftrBaseMarketplaceDetailsArgs]: ...
    @marketplace.setter
    def marketplace(self, value: pulumi.Input[LiftrBaseMarketplaceDetailsArgs]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[LiftrBaseUserDetailsArgs]: ...
    @user.setter
    def user(self, value: pulumi.Input[LiftrBaseUserDetailsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="partnerProperties")
    def partner_properties(self) -> Optional[pulumi.Input[PartnerPropertiesArgs]]: ...
    @partner_properties.setter
    def partner_properties(
        self, value: Optional[pulumi.Input[PartnerPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnProperties")
    def single_sign_on_properties(
        self,
    ) -> Optional[pulumi.Input[LiftrBaseSingleSignOnPropertiesV2Args]]: ...
    @single_sign_on_properties.setter
    def single_sign_on_properties(
        self, value: Optional[pulumi.Input[LiftrBaseSingleSignOnPropertiesV2Args]]
    ): ...

class LiftrBaseMarketplaceDetailsArgsDict(TypedDict):
    offer_details: pulumi.Input[LiftrBaseOfferDetailsArgsDict]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LiftrBaseMarketplaceDetailsArgs:
    def __init__(
        __self__,
        *,
        offer_details: pulumi.Input[LiftrBaseOfferDetailsArgs],
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="offerDetails")
    def offer_details(self) -> pulumi.Input[LiftrBaseOfferDetailsArgs]: ...
    @offer_details.setter
    def offer_details(self, value: pulumi.Input[LiftrBaseOfferDetailsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LiftrBaseOfferDetailsArgsDict(TypedDict):
    offer_id: pulumi.Input[_builtins.str]
    plan_id: pulumi.Input[_builtins.str]
    publisher_id: pulumi.Input[_builtins.str]
    plan_name: NotRequired[pulumi.Input[_builtins.str]]
    term_id: NotRequired[pulumi.Input[_builtins.str]]
    term_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LiftrBaseOfferDetailsArgs:
    def __init__(
        __self__,
        *,
        offer_id: pulumi.Input[_builtins.str],
        plan_id: pulumi.Input[_builtins.str],
        publisher_id: pulumi.Input[_builtins.str],
        plan_name: Optional[pulumi.Input[_builtins.str]] = ...,
        term_id: Optional[pulumi.Input[_builtins.str]] = ...,
        term_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> pulumi.Input[_builtins.str]: ...
    @offer_id.setter
    def offer_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Input[_builtins.str]: ...
    @plan_id.setter
    def plan_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> pulumi.Input[_builtins.str]: ...
    @publisher_id.setter
    def publisher_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="planName")
    def plan_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plan_name.setter
    def plan_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="termId")
    def term_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @term_id.setter
    def term_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @term_unit.setter
    def term_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LiftrBaseSingleSignOnPropertiesV2ArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, SingleSignOnType]]
    aad_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enterprise_app_id: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, SingleSignOnStates]]]
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LiftrBaseSingleSignOnPropertiesV2Args:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, SingleSignOnType]],
        aad_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enterprise_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, SingleSignOnStates]]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, SingleSignOnType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, SingleSignOnType]]): ...
    @_builtins.property
    @pulumi.getter(name="aadDomains")
    def aad_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aad_domains.setter
    def aad_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enterpriseAppId")
    def enterprise_app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enterprise_app_id.setter
    def enterprise_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SingleSignOnStates]]]: ...
    @state.setter
    def state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SingleSignOnStates]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LiftrBaseUserDetailsArgsDict(TypedDict):
    email_address: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    upn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LiftrBaseUserDetailsArgs:
    def __init__(
        __self__,
        *,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        upn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def upn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upn.setter
    def upn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PartnerPropertiesArgsDict(TypedDict):
    region: pulumi.Input[Union[_builtins.str, Region]]
    subdomain: pulumi.Input[_builtins.str]

@pulumi.input_type
class PartnerPropertiesArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[Union[_builtins.str, Region]],
        subdomain: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[Union[_builtins.str, Region]]: ...
    @region.setter
    def region(self, value: pulumi.Input[Union[_builtins.str, Region]]): ...
    @_builtins.property
    @pulumi.getter
    def subdomain(self) -> pulumi.Input[_builtins.str]: ...
    @subdomain.setter
    def subdomain(self, value: pulumi.Input[_builtins.str]): ...

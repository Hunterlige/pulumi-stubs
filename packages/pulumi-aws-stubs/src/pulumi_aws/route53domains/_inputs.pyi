

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DelegationSignerRecordSigningAttributesArgs', 'DelegationSignerRecordSigningAttributesArgsDict', 'DelegationSignerRecordTimeoutsArgs', 'DelegationSignerRecordTimeoutsArgsDict', 'DomainAdminContactArgs', 'DomainAdminContactArgsDict', 'DomainAdminContactExtraParamArgs', 'DomainAdminContactExtraParamArgsDict', 'DomainBillingContactArgs', 'DomainBillingContactArgsDict', 'DomainBillingContactExtraParamArgs', 'DomainBillingContactExtraParamArgsDict', 'DomainNameServerArgs', 'DomainNameServerArgsDict', 'DomainRegistrantContactArgs', 'DomainRegistrantContactArgsDict', 'DomainRegistrantContactExtraParamArgs', 'DomainRegistrantContactExtraParamArgsDict', 'DomainTechContactArgs', 'DomainTechContactArgsDict', 'DomainTechContactExtraParamArgs', 'DomainTechContactExtraParamArgsDict', 'DomainTimeoutsArgs', 'DomainTimeoutsArgsDict', 'RegisteredDomainAdminContactArgs', 'RegisteredDomainAdminContactArgsDict', 'RegisteredDomainBillingContactArgs', 'RegisteredDomainBillingContactArgsDict', 'RegisteredDomainNameServerArgs', 'RegisteredDomainNameServerArgsDict', 'RegisteredDomainRegistrantContactArgs', 'RegisteredDomainRegistrantContactArgsDict', 'RegisteredDomainTechContactArgs', 'RegisteredDomainTechContactArgsDict']
class DelegationSignerRecordSigningAttributesArgsDict(TypedDict):
    algorithm: pulumi.Input[_builtins.int]
    flags: pulumi.Input[_builtins.int]
    public_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class DelegationSignerRecordSigningAttributesArgs:
    def __init__(__self__, *, algorithm: pulumi.Input[_builtins.int], flags: pulumi.Input[_builtins.int], public_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @algorithm.setter
    def algorithm(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @flags.setter
    def flags(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DelegationSignerRecordTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DelegationSignerRecordTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainAdminContactArgsDict(TypedDict):
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    contact_type: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    extra_params: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainAdminContactExtraParamArgsDict]]]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainAdminContactArgs:
    def __init__(__self__, *, address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., contact_type: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., extra_params: Optional[pulumi.Input[Sequence[pulumi.Input[DomainAdminContactExtraParamArgs]]]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., zip_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainAdminContactExtraParamArgs]]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainAdminContactExtraParamArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainAdminContactExtraParamArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainAdminContactExtraParamArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainBillingContactArgsDict(TypedDict):
    address_line1: pulumi.Input[_builtins.str]
    address_line2: pulumi.Input[_builtins.str]
    city: pulumi.Input[_builtins.str]
    contact_type: pulumi.Input[_builtins.str]
    country_code: pulumi.Input[_builtins.str]
    email: pulumi.Input[_builtins.str]
    extra_params: pulumi.Input[Sequence[pulumi.Input[DomainBillingContactExtraParamArgsDict]]]
    fax: pulumi.Input[_builtins.str]
    first_name: pulumi.Input[_builtins.str]
    last_name: pulumi.Input[_builtins.str]
    organization_name: pulumi.Input[_builtins.str]
    phone_number: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    zip_code: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainBillingContactArgs:
    def __init__(__self__, *, address_line1: pulumi.Input[_builtins.str], address_line2: pulumi.Input[_builtins.str], city: pulumi.Input[_builtins.str], contact_type: pulumi.Input[_builtins.str], country_code: pulumi.Input[_builtins.str], email: pulumi.Input[_builtins.str], extra_params: pulumi.Input[Sequence[pulumi.Input[DomainBillingContactExtraParamArgs]]], fax: pulumi.Input[_builtins.str], first_name: pulumi.Input[_builtins.str], last_name: pulumi.Input[_builtins.str], organization_name: pulumi.Input[_builtins.str], phone_number: pulumi.Input[_builtins.str], state: pulumi.Input[_builtins.str], zip_code: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @city.setter
    def city(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> pulumi.Input[Sequence[pulumi.Input[DomainBillingContactExtraParamArgs]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: pulumi.Input[Sequence[pulumi.Input[DomainBillingContactExtraParamArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fax.setter
    def fax(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainBillingContactExtraParamArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainBillingContactExtraParamArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainNameServerArgsDict(TypedDict):
    glue_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainNameServerArgs:
    def __init__(__self__, *, glue_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueIps")
    def glue_ips(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @glue_ips.setter
    def glue_ips(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainRegistrantContactArgsDict(TypedDict):
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    contact_type: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    extra_params: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainRegistrantContactExtraParamArgsDict]]]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainRegistrantContactArgs:
    def __init__(__self__, *, address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., contact_type: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., extra_params: Optional[pulumi.Input[Sequence[pulumi.Input[DomainRegistrantContactExtraParamArgs]]]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., zip_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainRegistrantContactExtraParamArgs]]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainRegistrantContactExtraParamArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainRegistrantContactExtraParamArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainRegistrantContactExtraParamArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainTechContactArgsDict(TypedDict):
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    contact_type: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    extra_params: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainTechContactExtraParamArgsDict]]]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainTechContactArgs:
    def __init__(__self__, *, address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., contact_type: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., extra_params: Optional[pulumi.Input[Sequence[pulumi.Input[DomainTechContactExtraParamArgs]]]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., zip_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainTechContactExtraParamArgs]]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainTechContactExtraParamArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainTechContactExtraParamArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainTechContactExtraParamArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegisteredDomainAdminContactArgsDict(TypedDict):
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    contact_type: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegisteredDomainAdminContactArgs:
    def __init__(__self__, *, address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., contact_type: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., zip_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegisteredDomainBillingContactArgsDict(TypedDict):
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    contact_type: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegisteredDomainBillingContactArgs:
    def __init__(__self__, *, address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., contact_type: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., zip_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegisteredDomainNameServerArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    glue_ips: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RegisteredDomainNameServerArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], glue_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueIps")
    def glue_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @glue_ips.setter
    def glue_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RegisteredDomainRegistrantContactArgsDict(TypedDict):
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    contact_type: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegisteredDomainRegistrantContactArgs:
    def __init__(__self__, *, address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., contact_type: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., zip_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegisteredDomainTechContactArgsDict(TypedDict):
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    contact_type: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegisteredDomainTechContactArgs:
    def __init__(__self__, *, address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., contact_type: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., zip_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



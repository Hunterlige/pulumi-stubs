

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AddressArgs', 'AddressArgsDict', 'ContactArgs', 'ContactArgsDict', 'DomainPurchaseConsentArgs', 'DomainPurchaseConsentArgsDict']
class AddressArgsDict(TypedDict):
    
    address1: pulumi.Input[_builtins.str]
    city: pulumi.Input[_builtins.str]
    country: pulumi.Input[_builtins.str]
    postal_code: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    address2: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AddressArgs:
    def __init__(__self__, *, address1: pulumi.Input[_builtins.str], city: pulumi.Input[_builtins.str], country: pulumi.Input[_builtins.str], postal_code: pulumi.Input[_builtins.str], state: pulumi.Input[_builtins.str], address2: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address1(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address1.setter
    def address1(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @city.setter
    def city(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @country.setter
    def country(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address2.setter
    def address2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContactArgsDict(TypedDict):
    
    email: pulumi.Input[_builtins.str]
    name_first: pulumi.Input[_builtins.str]
    name_last: pulumi.Input[_builtins.str]
    phone: pulumi.Input[_builtins.str]
    address_mailing: NotRequired[pulumi.Input[AddressArgsDict]]
    fax: NotRequired[pulumi.Input[_builtins.str]]
    job_title: NotRequired[pulumi.Input[_builtins.str]]
    name_middle: NotRequired[pulumi.Input[_builtins.str]]
    organization: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContactArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], name_first: pulumi.Input[_builtins.str], name_last: pulumi.Input[_builtins.str], phone: pulumi.Input[_builtins.str], address_mailing: Optional[pulumi.Input[AddressArgs]] = ..., fax: Optional[pulumi.Input[_builtins.str]] = ..., job_title: Optional[pulumi.Input[_builtins.str]] = ..., name_middle: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameFirst")
    def name_first(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name_first.setter
    def name_first(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameLast")
    def name_last(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name_last.setter
    def name_last(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone.setter
    def phone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressMailing")
    def address_mailing(self) -> Optional[pulumi.Input[AddressArgs]]:
        
        ...
    
    @address_mailing.setter
    def address_mailing(self, value: Optional[pulumi.Input[AddressArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax.setter
    def fax(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobTitle")
    def job_title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_title.setter
    def job_title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameMiddle")
    def name_middle(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_middle.setter
    def name_middle(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainPurchaseConsentArgsDict(TypedDict):
    
    agreed_at: NotRequired[pulumi.Input[_builtins.str]]
    agreed_by: NotRequired[pulumi.Input[_builtins.str]]
    agreement_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainPurchaseConsentArgs:
    def __init__(__self__, *, agreed_at: Optional[pulumi.Input[_builtins.str]] = ..., agreed_by: Optional[pulumi.Input[_builtins.str]] = ..., agreement_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreedAt")
    def agreed_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agreed_at.setter
    def agreed_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreedBy")
    def agreed_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agreed_by.setter
    def agreed_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreementKeys")
    def agreement_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @agreement_keys.setter
    def agreement_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    



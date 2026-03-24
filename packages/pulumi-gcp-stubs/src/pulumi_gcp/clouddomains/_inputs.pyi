

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegistrationContactSettingsArgs', 'RegistrationContactSettingsArgsDict', 'RegistrationContactSettingsAdminContactArgs', 'RegistrationContactSettingsAdminContactArgsDict', ..., ..., 'RegistrationContactSettingsRegistrantContactArgs', ..., ..., ..., 'RegistrationContactSettingsTechnicalContactArgs', ..., ..., ..., 'RegistrationDnsSettingsArgs', 'RegistrationDnsSettingsArgsDict', 'RegistrationDnsSettingsCustomDnsArgs', 'RegistrationDnsSettingsCustomDnsArgsDict', 'RegistrationDnsSettingsCustomDnsDsRecordArgs', 'RegistrationDnsSettingsCustomDnsDsRecordArgsDict', 'RegistrationDnsSettingsGlueRecordArgs', 'RegistrationDnsSettingsGlueRecordArgsDict', 'RegistrationManagementSettingsArgs', 'RegistrationManagementSettingsArgsDict', 'RegistrationYearlyPriceArgs', 'RegistrationYearlyPriceArgsDict']
class RegistrationContactSettingsArgsDict(TypedDict):
    admin_contact: pulumi.Input[RegistrationContactSettingsAdminContactArgsDict]
    privacy: pulumi.Input[_builtins.str]
    registrant_contact: pulumi.Input[RegistrationContactSettingsRegistrantContactArgsDict]
    technical_contact: pulumi.Input[RegistrationContactSettingsTechnicalContactArgsDict]


@pulumi.input_type
class RegistrationContactSettingsArgs:
    def __init__(__self__, *, admin_contact: pulumi.Input[RegistrationContactSettingsAdminContactArgs], privacy: pulumi.Input[_builtins.str], registrant_contact: pulumi.Input[RegistrationContactSettingsRegistrantContactArgs], technical_contact: pulumi.Input[RegistrationContactSettingsTechnicalContactArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminContact")
    def admin_contact(self) -> pulumi.Input[RegistrationContactSettingsAdminContactArgs]:
        
        ...
    
    @admin_contact.setter
    def admin_contact(self, value: pulumi.Input[RegistrationContactSettingsAdminContactArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def privacy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @privacy.setter
    def privacy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantContact")
    def registrant_contact(self) -> pulumi.Input[RegistrationContactSettingsRegistrantContactArgs]:
        
        ...
    
    @registrant_contact.setter
    def registrant_contact(self, value: pulumi.Input[RegistrationContactSettingsRegistrantContactArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="technicalContact")
    def technical_contact(self) -> pulumi.Input[RegistrationContactSettingsTechnicalContactArgs]:
        
        ...
    
    @technical_contact.setter
    def technical_contact(self, value: pulumi.Input[RegistrationContactSettingsTechnicalContactArgs]): # -> None:
        ...
    


class RegistrationContactSettingsAdminContactArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    phone_number: pulumi.Input[_builtins.str]
    postal_address: pulumi.Input[RegistrationContactSettingsAdminContactPostalAddressArgsDict]
    fax_number: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistrationContactSettingsAdminContactArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], phone_number: pulumi.Input[_builtins.str], postal_address: pulumi.Input[RegistrationContactSettingsAdminContactPostalAddressArgs], fax_number: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> pulumi.Input[RegistrationContactSettingsAdminContactPostalAddressArgs]:
        
        ...
    
    @postal_address.setter
    def postal_address(self, value: pulumi.Input[RegistrationContactSettingsAdminContactPostalAddressArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="faxNumber")
    def fax_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax_number.setter
    def fax_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegistrationContactSettingsAdminContactPostalAddressArgsDict(TypedDict):
    region_code: pulumi.Input[_builtins.str]
    address_lines: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    administrative_area: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    organization: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    recipients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RegistrationContactSettingsAdminContactPostalAddressArgs:
    def __init__(__self__, *, region_code: pulumi.Input[_builtins.str], address_lines: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., administrative_area: Optional[pulumi.Input[_builtins.str]] = ..., locality: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_code.setter
    def region_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLines")
    def address_lines(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @address_lines.setter
    def address_lines(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeArea")
    def administrative_area(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administrative_area.setter
    def administrative_area(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recipients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @recipients.setter
    def recipients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RegistrationContactSettingsRegistrantContactArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    phone_number: pulumi.Input[_builtins.str]
    postal_address: pulumi.Input[RegistrationContactSettingsRegistrantContactPostalAddressArgsDict]
    fax_number: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistrationContactSettingsRegistrantContactArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], phone_number: pulumi.Input[_builtins.str], postal_address: pulumi.Input[RegistrationContactSettingsRegistrantContactPostalAddressArgs], fax_number: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> pulumi.Input[RegistrationContactSettingsRegistrantContactPostalAddressArgs]:
        
        ...
    
    @postal_address.setter
    def postal_address(self, value: pulumi.Input[RegistrationContactSettingsRegistrantContactPostalAddressArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="faxNumber")
    def fax_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax_number.setter
    def fax_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegistrationContactSettingsRegistrantContactPostalAddressArgsDict(TypedDict):
    region_code: pulumi.Input[_builtins.str]
    address_lines: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    administrative_area: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    organization: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    recipients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RegistrationContactSettingsRegistrantContactPostalAddressArgs:
    def __init__(__self__, *, region_code: pulumi.Input[_builtins.str], address_lines: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., administrative_area: Optional[pulumi.Input[_builtins.str]] = ..., locality: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_code.setter
    def region_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLines")
    def address_lines(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @address_lines.setter
    def address_lines(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeArea")
    def administrative_area(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administrative_area.setter
    def administrative_area(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recipients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @recipients.setter
    def recipients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RegistrationContactSettingsTechnicalContactArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    phone_number: pulumi.Input[_builtins.str]
    postal_address: pulumi.Input[RegistrationContactSettingsTechnicalContactPostalAddressArgsDict]
    fax_number: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistrationContactSettingsTechnicalContactArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], phone_number: pulumi.Input[_builtins.str], postal_address: pulumi.Input[RegistrationContactSettingsTechnicalContactPostalAddressArgs], fax_number: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> pulumi.Input[RegistrationContactSettingsTechnicalContactPostalAddressArgs]:
        
        ...
    
    @postal_address.setter
    def postal_address(self, value: pulumi.Input[RegistrationContactSettingsTechnicalContactPostalAddressArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="faxNumber")
    def fax_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fax_number.setter
    def fax_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegistrationContactSettingsTechnicalContactPostalAddressArgsDict(TypedDict):
    region_code: pulumi.Input[_builtins.str]
    address_lines: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    administrative_area: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    organization: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    recipients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RegistrationContactSettingsTechnicalContactPostalAddressArgs:
    def __init__(__self__, *, region_code: pulumi.Input[_builtins.str], address_lines: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., administrative_area: Optional[pulumi.Input[_builtins.str]] = ..., locality: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_code.setter
    def region_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLines")
    def address_lines(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @address_lines.setter
    def address_lines(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeArea")
    def administrative_area(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administrative_area.setter
    def administrative_area(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recipients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @recipients.setter
    def recipients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RegistrationDnsSettingsArgsDict(TypedDict):
    custom_dns: NotRequired[pulumi.Input[RegistrationDnsSettingsCustomDnsArgsDict]]
    glue_records: NotRequired[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsGlueRecordArgsDict]]]]


@pulumi.input_type
class RegistrationDnsSettingsArgs:
    def __init__(__self__, *, custom_dns: Optional[pulumi.Input[RegistrationDnsSettingsCustomDnsArgs]] = ..., glue_records: Optional[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsGlueRecordArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDns")
    def custom_dns(self) -> Optional[pulumi.Input[RegistrationDnsSettingsCustomDnsArgs]]:
        
        ...
    
    @custom_dns.setter
    def custom_dns(self, value: Optional[pulumi.Input[RegistrationDnsSettingsCustomDnsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueRecords")
    def glue_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsGlueRecordArgs]]]]:
        
        ...
    
    @glue_records.setter
    def glue_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsGlueRecordArgs]]]]): # -> None:
        ...
    


class RegistrationDnsSettingsCustomDnsArgsDict(TypedDict):
    name_servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ds_records: NotRequired[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsCustomDnsDsRecordArgsDict]]]]


@pulumi.input_type
class RegistrationDnsSettingsCustomDnsArgs:
    def __init__(__self__, *, name_servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], ds_records: Optional[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsCustomDnsDsRecordArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @name_servers.setter
    def name_servers(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dsRecords")
    def ds_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsCustomDnsDsRecordArgs]]]]:
        
        ...
    
    @ds_records.setter
    def ds_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegistrationDnsSettingsCustomDnsDsRecordArgs]]]]): # -> None:
        ...
    


class RegistrationDnsSettingsCustomDnsDsRecordArgsDict(TypedDict):
    algorithm: NotRequired[pulumi.Input[_builtins.str]]
    digest: NotRequired[pulumi.Input[_builtins.str]]
    digest_type: NotRequired[pulumi.Input[_builtins.str]]
    key_tag: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class RegistrationDnsSettingsCustomDnsDsRecordArgs:
    def __init__(__self__, *, algorithm: Optional[pulumi.Input[_builtins.str]] = ..., digest: Optional[pulumi.Input[_builtins.str]] = ..., digest_type: Optional[pulumi.Input[_builtins.str]] = ..., key_tag: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @digest.setter
    def digest(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestType")
    def digest_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @digest_type.setter
    def digest_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @key_tag.setter
    def key_tag(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class RegistrationDnsSettingsGlueRecordArgsDict(TypedDict):
    host_name: pulumi.Input[_builtins.str]
    ipv4_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv6_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RegistrationDnsSettingsGlueRecordArgs:
    def __init__(__self__, *, host_name: pulumi.Input[_builtins.str], ipv4_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv4_addresses.setter
    def ipv4_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RegistrationManagementSettingsArgsDict(TypedDict):
    preferred_renewal_method: NotRequired[pulumi.Input[_builtins.str]]
    renewal_method: NotRequired[pulumi.Input[_builtins.str]]
    transfer_lock_state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistrationManagementSettingsArgs:
    def __init__(__self__, *, preferred_renewal_method: Optional[pulumi.Input[_builtins.str]] = ..., renewal_method: Optional[pulumi.Input[_builtins.str]] = ..., transfer_lock_state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredRenewalMethod")
    def preferred_renewal_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_renewal_method.setter
    def preferred_renewal_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalMethod")
    def renewal_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @renewal_method.setter
    def renewal_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferLockState")
    def transfer_lock_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transfer_lock_state.setter
    def transfer_lock_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegistrationYearlyPriceArgsDict(TypedDict):
    currency_code: NotRequired[pulumi.Input[_builtins.str]]
    units: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistrationYearlyPriceArgs:
    def __init__(__self__, *, currency_code: Optional[pulumi.Input[_builtins.str]] = ..., units: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @currency_code.setter
    def currency_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def units(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @units.setter
    def units(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



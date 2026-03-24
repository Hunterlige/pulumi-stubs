

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegistrationContactSettings', 'RegistrationContactSettingsAdminContact', ..., 'RegistrationContactSettingsRegistrantContact', ..., 'RegistrationContactSettingsTechnicalContact', ..., 'RegistrationDnsSettings', 'RegistrationDnsSettingsCustomDns', 'RegistrationDnsSettingsCustomDnsDsRecord', 'RegistrationDnsSettingsGlueRecord', 'RegistrationManagementSettings', 'RegistrationYearlyPrice']
@pulumi.output_type
class RegistrationContactSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_contact: outputs.RegistrationContactSettingsAdminContact, privacy: _builtins.str, registrant_contact: outputs.RegistrationContactSettingsRegistrantContact, technical_contact: outputs.RegistrationContactSettingsTechnicalContact) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminContact")
    def admin_contact(self) -> outputs.RegistrationContactSettingsAdminContact:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def privacy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrantContact")
    def registrant_contact(self) -> outputs.RegistrationContactSettingsRegistrantContact:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="technicalContact")
    def technical_contact(self) -> outputs.RegistrationContactSettingsTechnicalContact:
        
        ...
    


@pulumi.output_type
class RegistrationContactSettingsAdminContact(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email: _builtins.str, phone_number: _builtins.str, postal_address: outputs.RegistrationContactSettingsAdminContactPostalAddress, fax_number: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> outputs.RegistrationContactSettingsAdminContactPostalAddress:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="faxNumber")
    def fax_number(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegistrationContactSettingsAdminContactPostalAddress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, region_code: _builtins.str, address_lines: Optional[Sequence[_builtins.str]] = ..., administrative_area: Optional[_builtins.str] = ..., locality: Optional[_builtins.str] = ..., organization: Optional[_builtins.str] = ..., postal_code: Optional[_builtins.str] = ..., recipients: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLines")
    def address_lines(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeArea")
    def administrative_area(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recipients(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RegistrationContactSettingsRegistrantContact(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email: _builtins.str, phone_number: _builtins.str, postal_address: outputs.RegistrationContactSettingsRegistrantContactPostalAddress, fax_number: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> outputs.RegistrationContactSettingsRegistrantContactPostalAddress:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="faxNumber")
    def fax_number(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegistrationContactSettingsRegistrantContactPostalAddress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, region_code: _builtins.str, address_lines: Optional[Sequence[_builtins.str]] = ..., administrative_area: Optional[_builtins.str] = ..., locality: Optional[_builtins.str] = ..., organization: Optional[_builtins.str] = ..., postal_code: Optional[_builtins.str] = ..., recipients: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLines")
    def address_lines(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeArea")
    def administrative_area(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recipients(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RegistrationContactSettingsTechnicalContact(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email: _builtins.str, phone_number: _builtins.str, postal_address: outputs.RegistrationContactSettingsTechnicalContactPostalAddress, fax_number: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> outputs.RegistrationContactSettingsTechnicalContactPostalAddress:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="faxNumber")
    def fax_number(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegistrationContactSettingsTechnicalContactPostalAddress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, region_code: _builtins.str, address_lines: Optional[Sequence[_builtins.str]] = ..., administrative_area: Optional[_builtins.str] = ..., locality: Optional[_builtins.str] = ..., organization: Optional[_builtins.str] = ..., postal_code: Optional[_builtins.str] = ..., recipients: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLines")
    def address_lines(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeArea")
    def administrative_area(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recipients(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RegistrationDnsSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_dns: Optional[outputs.RegistrationDnsSettingsCustomDns] = ..., glue_records: Optional[Sequence[outputs.RegistrationDnsSettingsGlueRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDns")
    def custom_dns(self) -> Optional[outputs.RegistrationDnsSettingsCustomDns]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueRecords")
    def glue_records(self) -> Optional[Sequence[outputs.RegistrationDnsSettingsGlueRecord]]:
        
        ...
    


@pulumi.output_type
class RegistrationDnsSettingsCustomDns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name_servers: Sequence[_builtins.str], ds_records: Optional[Sequence[outputs.RegistrationDnsSettingsCustomDnsDsRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dsRecords")
    def ds_records(self) -> Optional[Sequence[outputs.RegistrationDnsSettingsCustomDnsDsRecord]]:
        
        ...
    


@pulumi.output_type
class RegistrationDnsSettingsCustomDnsDsRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, algorithm: Optional[_builtins.str] = ..., digest: Optional[_builtins.str] = ..., digest_type: Optional[_builtins.str] = ..., key_tag: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestType")
    def digest_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RegistrationDnsSettingsGlueRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, host_name: _builtins.str, ipv4_addresses: Optional[Sequence[_builtins.str]] = ..., ipv6_addresses: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RegistrationManagementSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, preferred_renewal_method: Optional[_builtins.str] = ..., renewal_method: Optional[_builtins.str] = ..., transfer_lock_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredRenewalMethod")
    def preferred_renewal_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalMethod")
    def renewal_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferLockState")
    def transfer_lock_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegistrationYearlyPrice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, currency_code: Optional[_builtins.str] = ..., units: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def units(self) -> Optional[_builtins.str]:
        
        ...
    



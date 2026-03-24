import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DelegationSignerRecordSigningAttributes",
    "DelegationSignerRecordTimeouts",
    "DomainAdminContact",
    "DomainAdminContactExtraParam",
    "DomainBillingContact",
    "DomainBillingContactExtraParam",
    "DomainNameServer",
    "DomainRegistrantContact",
    "DomainRegistrantContactExtraParam",
    "DomainTechContact",
    "DomainTechContactExtraParam",
    "DomainTimeouts",
    "RegisteredDomainAdminContact",
    "RegisteredDomainBillingContact",
    "RegisteredDomainNameServer",
    "RegisteredDomainRegistrantContact",
    "RegisteredDomainTechContact",
]

@pulumi.output_type
class DelegationSignerRecordSigningAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm: _builtins.int,
        flags: _builtins.int,
        public_key: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str: ...

@pulumi.output_type
class DelegationSignerRecordTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainAdminContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        contact_type: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        extra_params: Optional[Sequence[outputs.DomainAdminContactExtraParam]] = ...,
        fax: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        organization_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        zip_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(
        self,
    ) -> Optional[Sequence[outputs.DomainAdminContactExtraParam]]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainAdminContactExtraParam(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class DomainBillingContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: _builtins.str,
        address_line2: _builtins.str,
        city: _builtins.str,
        contact_type: _builtins.str,
        country_code: _builtins.str,
        email: _builtins.str,
        extra_params: Sequence[outputs.DomainBillingContactExtraParam],
        fax: _builtins.str,
        first_name: _builtins.str,
        last_name: _builtins.str,
        organization_name: _builtins.str,
        phone_number: _builtins.str,
        state: _builtins.str,
        zip_code: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Sequence[outputs.DomainBillingContactExtraParam]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> _builtins.str: ...

@pulumi.output_type
class DomainBillingContactExtraParam(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class DomainNameServer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, glue_ips: Sequence[_builtins.str], name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="glueIps")
    def glue_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class DomainRegistrantContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        contact_type: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        extra_params: Optional[
            Sequence[outputs.DomainRegistrantContactExtraParam]
        ] = ...,
        fax: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        organization_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        zip_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(
        self,
    ) -> Optional[Sequence[outputs.DomainRegistrantContactExtraParam]]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainRegistrantContactExtraParam(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class DomainTechContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        contact_type: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        extra_params: Optional[Sequence[outputs.DomainTechContactExtraParam]] = ...,
        fax: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        organization_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        zip_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(
        self,
    ) -> Optional[Sequence[outputs.DomainTechContactExtraParam]]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainTechContactExtraParam(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class DomainTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegisteredDomainAdminContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        contact_type: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        extra_params: Optional[Mapping[str, _builtins.str]] = ...,
        fax: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        organization_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        zip_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegisteredDomainBillingContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        contact_type: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        extra_params: Optional[Mapping[str, _builtins.str]] = ...,
        fax: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        organization_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        zip_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegisteredDomainNameServer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        glue_ips: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="glueIps")
    def glue_ips(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RegisteredDomainRegistrantContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        contact_type: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        extra_params: Optional[Mapping[str, _builtins.str]] = ...,
        fax: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        organization_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        zip_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegisteredDomainTechContact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        contact_type: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        extra_params: Optional[Mapping[str, _builtins.str]] = ...,
        fax: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        organization_name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        zip_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[_builtins.str]: ...

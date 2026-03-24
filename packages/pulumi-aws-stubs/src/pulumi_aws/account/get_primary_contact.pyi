import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrimaryContactResult",
    "AwaitableGetPrimaryContactResult",
    "get_primary_contact",
    "get_primary_contact_output",
]

@pulumi.output_type
class GetPrimaryContactResult:
    def __init__(
        __self__,
        account_id=...,
        address_line1=...,
        address_line2=...,
        address_line3=...,
        city=...,
        company_name=...,
        country_code=...,
        district_or_county=...,
        full_name=...,
        id=...,
        phone_number=...,
        postal_code=...,
        state_or_region=...,
        website_url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="districtOrCounty")
    def district_or_county(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stateOrRegion")
    def state_or_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="websiteUrl")
    def website_url(self) -> _builtins.str: ...

class AwaitableGetPrimaryContactResult(GetPrimaryContactResult):
    def __await__(self):  # -> Generator[Never, Any, GetPrimaryContactResult]:
        ...

def get_primary_contact(
    account_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrimaryContactResult: ...
def get_primary_contact_output(
    account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrimaryContactResult]: ...

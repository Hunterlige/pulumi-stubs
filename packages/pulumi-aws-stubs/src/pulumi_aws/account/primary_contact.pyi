

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrimaryContactArgs', 'PrimaryContact']
@pulumi.input_type
class PrimaryContactArgs:
    def __init__(__self__, *, address_line1: pulumi.Input[_builtins.str], city: pulumi.Input[_builtins.str], country_code: pulumi.Input[_builtins.str], full_name: pulumi.Input[_builtins.str], phone_number: pulumi.Input[_builtins.str], postal_code: pulumi.Input[_builtins.str], account_id: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., address_line3: Optional[pulumi.Input[_builtins.str]] = ..., company_name: Optional[pulumi.Input[_builtins.str]] = ..., district_or_county: Optional[pulumi.Input[_builtins.str]] = ..., state_or_region: Optional[pulumi.Input[_builtins.str]] = ..., website_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address_line1.setter
    def address_line1(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @city.setter
    def city(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @full_name.setter
    def full_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line3.setter
    def address_line3(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="districtOrCounty")
    def district_or_county(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @district_or_county.setter
    def district_or_county(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateOrRegion")
    def state_or_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_or_region.setter
    def state_or_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteUrl")
    def website_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @website_url.setter
    def website_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PrimaryContactState:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., address_line3: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., company_name: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., district_or_county: Optional[pulumi.Input[_builtins.str]] = ..., full_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., state_or_region: Optional[pulumi.Input[_builtins.str]] = ..., website_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_line3.setter
    def address_line3(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="districtOrCounty")
    def district_or_county(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @district_or_county.setter
    def district_or_county(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @full_name.setter
    def full_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateOrRegion")
    def state_or_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_or_region.setter
    def state_or_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteUrl")
    def website_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @website_url.setter
    def website_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:account/primaryContact:PrimaryContact")
class PrimaryContact(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., address_line3: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., company_name: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., district_or_county: Optional[pulumi.Input[_builtins.str]] = ..., full_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., state_or_region: Optional[pulumi.Input[_builtins.str]] = ..., website_url: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrimaryContactArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., address_line1: Optional[pulumi.Input[_builtins.str]] = ..., address_line2: Optional[pulumi.Input[_builtins.str]] = ..., address_line3: Optional[pulumi.Input[_builtins.str]] = ..., city: Optional[pulumi.Input[_builtins.str]] = ..., company_name: Optional[pulumi.Input[_builtins.str]] = ..., country_code: Optional[pulumi.Input[_builtins.str]] = ..., district_or_county: Optional[pulumi.Input[_builtins.str]] = ..., full_name: Optional[pulumi.Input[_builtins.str]] = ..., phone_number: Optional[pulumi.Input[_builtins.str]] = ..., postal_code: Optional[pulumi.Input[_builtins.str]] = ..., state_or_region: Optional[pulumi.Input[_builtins.str]] = ..., website_url: Optional[pulumi.Input[_builtins.str]] = ...) -> PrimaryContact:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="districtOrCounty")
    def district_or_county(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateOrRegion")
    def state_or_region(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteUrl")
    def website_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    



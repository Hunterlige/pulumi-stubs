

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GroupExternalId', 'UserAddresses', 'UserEmails', 'UserExternalId', 'UserName', 'UserPhoneNumbers', 'GetGroupAlternateIdentifierResult', 'GetGroupAlternateIdentifierExternalIdResult', 'GetGroupAlternateIdentifierUniqueAttributeResult', 'GetGroupExternalIdResult', 'GetGroupMembershipsGroupMembershipResult', 'GetGroupMembershipsGroupMembershipMemberIdResult', 'GetGroupsGroupResult', 'GetGroupsGroupExternalIdResult', 'GetUserAddressResult', 'GetUserAlternateIdentifierResult', 'GetUserAlternateIdentifierExternalIdResult', 'GetUserAlternateIdentifierUniqueAttributeResult', 'GetUserEmailResult', 'GetUserExternalIdResult', 'GetUserNameResult', 'GetUserPhoneNumberResult', 'GetUsersUserResult', 'GetUsersUserAddressResult', 'GetUsersUserEmailResult', 'GetUsersUserExternalIdResult', 'GetUsersUserNameResult', 'GetUsersUserPhoneNumberResult']
@pulumi.output_type
class GroupExternalId(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., issuer: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserAddresses(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, country: Optional[_builtins.str] = ..., formatted: Optional[_builtins.str] = ..., locality: Optional[_builtins.str] = ..., postal_code: Optional[_builtins.str] = ..., primary: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., street_address: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserEmails(dict):
    def __init__(__self__, *, primary: Optional[_builtins.bool] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserExternalId(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., issuer: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserName(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, family_name: _builtins.str, given_name: _builtins.str, formatted: Optional[_builtins.str] = ..., honorific_prefix: Optional[_builtins.str] = ..., honorific_suffix: Optional[_builtins.str] = ..., middle_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="familyName")
    def family_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="givenName")
    def given_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPhoneNumbers(dict):
    def __init__(__self__, *, primary: Optional[_builtins.bool] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetGroupAlternateIdentifierResult(dict):
    def __init__(__self__, *, external_id: Optional[outputs.GetGroupAlternateIdentifierExternalIdResult] = ..., unique_attribute: Optional[outputs.GetGroupAlternateIdentifierUniqueAttributeResult] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[outputs.GetGroupAlternateIdentifierExternalIdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(self) -> Optional[outputs.GetGroupAlternateIdentifierUniqueAttributeResult]:
        
        ...
    


@pulumi.output_type
class GetGroupAlternateIdentifierExternalIdResult(dict):
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupAlternateIdentifierUniqueAttributeResult(dict):
    def __init__(__self__, *, attribute_path: _builtins.str, attribute_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupExternalIdResult(dict):
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMembershipsGroupMembershipResult(dict):
    def __init__(__self__, *, group_id: _builtins.str, identity_store_id: _builtins.str, member_id: outputs.GetGroupMembershipsGroupMembershipMemberIdResult, membership_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberId")
    def member_id(self) -> outputs.GetGroupMembershipsGroupMembershipMemberIdResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetGroupMembershipsGroupMembershipMemberIdResult(dict):
    def __init__(__self__, *, user_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupsGroupResult(dict):
    def __init__(__self__, *, description: _builtins.str, display_name: _builtins.str, external_ids: Sequence[outputs.GetGroupsGroupExternalIdResult], group_id: _builtins.str, identity_store_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIds")
    def external_ids(self) -> Sequence[outputs.GetGroupsGroupExternalIdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupsGroupExternalIdResult(dict):
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserAddressResult(dict):
    def __init__(__self__, *, country: _builtins.str, formatted: _builtins.str, locality: _builtins.str, postal_code: _builtins.str, primary: _builtins.bool, region: _builtins.str, street_address: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserAlternateIdentifierResult(dict):
    def __init__(__self__, *, external_id: Optional[outputs.GetUserAlternateIdentifierExternalIdResult] = ..., unique_attribute: Optional[outputs.GetUserAlternateIdentifierUniqueAttributeResult] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[outputs.GetUserAlternateIdentifierExternalIdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(self) -> Optional[outputs.GetUserAlternateIdentifierUniqueAttributeResult]:
        
        ...
    


@pulumi.output_type
class GetUserAlternateIdentifierExternalIdResult(dict):
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserAlternateIdentifierUniqueAttributeResult(dict):
    def __init__(__self__, *, attribute_path: _builtins.str, attribute_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserEmailResult(dict):
    def __init__(__self__, *, primary: _builtins.bool, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserExternalIdResult(dict):
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserNameResult(dict):
    def __init__(__self__, *, family_name: _builtins.str, formatted: _builtins.str, given_name: _builtins.str, honorific_prefix: _builtins.str, honorific_suffix: _builtins.str, middle_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="familyName")
    def family_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="givenName")
    def given_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUserPhoneNumberResult(dict):
    def __init__(__self__, *, primary: _builtins.bool, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUsersUserResult(dict):
    def __init__(__self__, *, addresses: Sequence[outputs.GetUsersUserAddressResult], display_name: _builtins.str, emails: Sequence[outputs.GetUsersUserEmailResult], external_ids: Sequence[outputs.GetUsersUserExternalIdResult], identity_store_id: _builtins.str, locale: _builtins.str, names: Sequence[outputs.GetUsersUserNameResult], nickname: _builtins.str, phone_numbers: Sequence[outputs.GetUsersUserPhoneNumberResult], preferred_language: _builtins.str, profile_url: _builtins.str, timezone: _builtins.str, title: _builtins.str, user_id: _builtins.str, user_name: _builtins.str, user_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[outputs.GetUsersUserAddressResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Sequence[outputs.GetUsersUserEmailResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIds")
    def external_ids(self) -> Sequence[outputs.GetUsersUserExternalIdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[outputs.GetUsersUserNameResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nickname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Sequence[outputs.GetUsersUserPhoneNumberResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredLanguage")
    def preferred_language(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileUrl")
    def profile_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUsersUserAddressResult(dict):
    def __init__(__self__, *, country: _builtins.str, formatted: _builtins.str, locality: _builtins.str, postal_code: _builtins.str, primary: _builtins.bool, region: _builtins.str, street_address: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUsersUserEmailResult(dict):
    def __init__(__self__, *, primary: _builtins.bool, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUsersUserExternalIdResult(dict):
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUsersUserNameResult(dict):
    def __init__(__self__, *, family_name: _builtins.str, formatted: _builtins.str, given_name: _builtins.str, honorific_prefix: _builtins.str, honorific_suffix: _builtins.str, middle_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="familyName")
    def family_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="givenName")
    def given_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUsersUserPhoneNumberResult(dict):
    def __init__(__self__, *, primary: _builtins.bool, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    



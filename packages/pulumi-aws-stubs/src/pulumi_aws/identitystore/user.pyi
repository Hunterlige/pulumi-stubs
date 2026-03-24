

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserArgs', 'User']
@pulumi.input_type
class UserArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], identity_store_id: pulumi.Input[_builtins.str], user_name: pulumi.Input[_builtins.str], addresses: Optional[pulumi.Input[UserAddressesArgs]] = ..., emails: Optional[pulumi.Input[UserEmailsArgs]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[UserNameArgs]] = ..., nickname: Optional[pulumi.Input[_builtins.str]] = ..., phone_numbers: Optional[pulumi.Input[UserPhoneNumbersArgs]] = ..., preferred_language: Optional[pulumi.Input[_builtins.str]] = ..., profile_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., user_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_store_id.setter
    def identity_store_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Optional[pulumi.Input[UserAddressesArgs]]:
        
        ...
    
    @addresses.setter
    def addresses(self, value: Optional[pulumi.Input[UserAddressesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Optional[pulumi.Input[UserEmailsArgs]]:
        
        ...
    
    @emails.setter
    def emails(self, value: Optional[pulumi.Input[UserEmailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[UserNameArgs]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[UserNameArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nickname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nickname.setter
    def nickname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Optional[pulumi.Input[UserPhoneNumbersArgs]]:
        
        ...
    
    @phone_numbers.setter
    def phone_numbers(self, value: Optional[pulumi.Input[UserPhoneNumbersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredLanguage")
    def preferred_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_language.setter
    def preferred_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileUrl")
    def profile_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @profile_url.setter
    def profile_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UserState:
    def __init__(__self__, *, addresses: Optional[pulumi.Input[UserAddressesArgs]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., emails: Optional[pulumi.Input[UserEmailsArgs]] = ..., external_ids: Optional[pulumi.Input[Sequence[pulumi.Input[UserExternalIdArgs]]]] = ..., identity_store_id: Optional[pulumi.Input[_builtins.str]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[UserNameArgs]] = ..., nickname: Optional[pulumi.Input[_builtins.str]] = ..., phone_numbers: Optional[pulumi.Input[UserPhoneNumbersArgs]] = ..., preferred_language: Optional[pulumi.Input[_builtins.str]] = ..., profile_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., user_id: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., user_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Optional[pulumi.Input[UserAddressesArgs]]:
        
        ...
    
    @addresses.setter
    def addresses(self, value: Optional[pulumi.Input[UserAddressesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Optional[pulumi.Input[UserEmailsArgs]]:
        
        ...
    
    @emails.setter
    def emails(self, value: Optional[pulumi.Input[UserEmailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIds")
    def external_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserExternalIdArgs]]]]:
        
        ...
    
    @external_ids.setter
    def external_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserExternalIdArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_store_id.setter
    def identity_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[UserNameArgs]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[UserNameArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nickname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nickname.setter
    def nickname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Optional[pulumi.Input[UserPhoneNumbersArgs]]:
        
        ...
    
    @phone_numbers.setter
    def phone_numbers(self, value: Optional[pulumi.Input[UserPhoneNumbersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredLanguage")
    def preferred_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_language.setter
    def preferred_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileUrl")
    def profile_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @profile_url.setter
    def profile_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:identitystore/user:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., addresses: Optional[pulumi.Input[Union[UserAddressesArgs, UserAddressesArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., emails: Optional[pulumi.Input[Union[UserEmailsArgs, UserEmailsArgsDict]]] = ..., identity_store_id: Optional[pulumi.Input[_builtins.str]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[Union[UserNameArgs, UserNameArgsDict]]] = ..., nickname: Optional[pulumi.Input[_builtins.str]] = ..., phone_numbers: Optional[pulumi.Input[Union[UserPhoneNumbersArgs, UserPhoneNumbersArgsDict]]] = ..., preferred_language: Optional[pulumi.Input[_builtins.str]] = ..., profile_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., user_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., addresses: Optional[pulumi.Input[Union[UserAddressesArgs, UserAddressesArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., emails: Optional[pulumi.Input[Union[UserEmailsArgs, UserEmailsArgsDict]]] = ..., external_ids: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UserExternalIdArgs, UserExternalIdArgsDict]]]]] = ..., identity_store_id: Optional[pulumi.Input[_builtins.str]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[Union[UserNameArgs, UserNameArgsDict]]] = ..., nickname: Optional[pulumi.Input[_builtins.str]] = ..., phone_numbers: Optional[pulumi.Input[Union[UserPhoneNumbersArgs, UserPhoneNumbersArgsDict]]] = ..., preferred_language: Optional[pulumi.Input[_builtins.str]] = ..., profile_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., user_id: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., user_type: Optional[pulumi.Input[_builtins.str]] = ...) -> User:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> pulumi.Output[Optional[outputs.UserAddresses]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> pulumi.Output[Optional[outputs.UserEmails]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIds")
    def external_ids(self) -> pulumi.Output[Sequence[outputs.UserExternalId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[outputs.UserName]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nickname(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> pulumi.Output[Optional[outputs.UserPhoneNumbers]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredLanguage")
    def preferred_language(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileUrl")
    def profile_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


